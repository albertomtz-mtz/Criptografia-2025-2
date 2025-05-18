# --- Constantes AES ---
# S-Box (sustitución no lineal)
s_box = [
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
]

# Rcon (constantes de ronda para Key Schedule)
rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]

# --- Funciones Auxiliares ---
def texto_a_matriz(texto):
    """Convierte un string de 16 bytes en matriz 4x4."""
    return [[ord(texto[i + 4 * j]) for i in range(4)] for j in range(4)]

def matriz_a_texto(matriz):
    """Convierte una matriz 4x4 en string."""
    return ''.join([chr(matriz[j][i]) for i in range(4) for j in range(4)])

def sub_bytes(state):
    """Aplica SubBytes a cada byte del estado."""
    return [[s_box[b] for b in row] for row in state]

def shift_rows(state):
    """Desplaza filas del estado."""
    return [
        [state[0][0], state[1][1], state[2][2], state[3][3]],
        [state[1][0], state[2][1], state[3][2], state[0][3]],
        [state[2][0], state[3][1], state[0][2], state[1][3]],
        [state[3][0], state[0][1], state[1][2], state[2][3]]
    ]

def galois_mult(a, b):
    """Multiplicación en GF(2^8)."""
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11B  # Polinomio irreducible
        b >>= 1
    return p

def mix_columns(state):
    """Mezcla columnas del estado."""
    new_state = [[0]*4 for _ in range(4)]
    for i in range(4):
        new_state[0][i] = galois_mult(0x02, state[0][i]) ^ galois_mult(0x03, state[1][i]) ^ state[2][i] ^ state[3][i]
        new_state[1][i] = state[0][i] ^ galois_mult(0x02, state[1][i]) ^ galois_mult(0x03, state[2][i]) ^ state[3][i]
        new_state[2][i] = state[0][i] ^ state[1][i] ^ galois_mult(0x02, state[2][i]) ^ galois_mult(0x03, state[3][i])
        new_state[3][i] = galois_mult(0x03, state[0][i]) ^ state[1][i] ^ state[2][i] ^ galois_mult(0x02, state[3][i])
    return new_state

def add_round_key(state, round_key):
    """XOR entre el estado y la clave de ronda."""
    return [[state[i][j] ^ round_key[i][j] for j in range(4)] for i in range(4)]

# --- Key Schedule (Expansión de Clave) ---
def rot_word(word):
    """Rota una palabra (fila) 1 byte a la izquierda."""
    return word[1:] + word[:1]

def sub_word(word):
    """Aplica S-Box a cada byte de una palabra."""
    return [s_box[b] for b in word]

def expand_key(key):
    """Genera las 11 subclaves para AES-128."""
    keys = [key]
    for i in range(10):
        # Primera palabra de la nueva subclave
        temp = [keys[i][j][3] for j in range(4)]  # Última columna
        temp = rot_word(temp)
        temp = sub_word(temp)
        temp[0] ^= rcon[i]
        
        new_key = [[0]*4 for _ in range(4)]
        for j in range(4):
            new_key[j][0] = keys[i][j][0] ^ temp[j]
            new_key[j][1] = keys[i][j][1] ^ new_key[j][0]
            new_key[j][2] = keys[i][j][2] ^ new_key[j][1]
            new_key[j][3] = keys[i][j][3] ^ new_key[j][2]
        keys.append(new_key)
    return keys

# --- Cifrado AES ---
def aes_encrypt(plaintext, key):
    """Cifra un bloque de 16 bytes con AES-128."""
    state = texto_a_matriz(plaintext)
    round_keys = expand_key(texto_a_matriz(key))
    
    # Ronda inicial (AddRoundKey)
    state = add_round_key(state, round_keys[0])
    
    # 9 rondas principales
    for i in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, round_keys[i])
    
    # Ronda final (sin MixColumns)
    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, round_keys[10])
    
    return matriz_a_texto(state)

# --- Ejemplo de Uso ---
plaintext = "Thats My Kung Fu"  # Mensaje del PDF
key = "Two One Nine Two"       # Clave del PDF

ciphertext = aes_encrypt(plaintext, key)
print("Texto cifrado (hex):", ' '.join(f'{ord(c):02X}' for c in ciphertext))