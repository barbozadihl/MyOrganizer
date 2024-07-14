import os
import shutil

# Função para criar uma pasta se ela não existir
def create_folder(folder_path):
    """Cria uma pasta se ela não existir"""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Função principal para organizar arquivos
def organize_files(folder_path):
    """Organiza arquivos no diretório com base em seus tipos"""
    # Define um dicionário para os tipos de arquivos comuns e suas respectivas pastas
    file_type_folders = {
        'Documentos': ['.pdf', '.docx', '.doc', '.xlsx', '.pptx', '.txt'],
        'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv'],
        'Audios': ['.mp3', '.wav', '.ogg', '.flac'],
        'Arquivos': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Executaveis': ['.exe', '.bat', '.sh'],
        'Scripts': ['.py', '.js', '.html', '.css'],
        'Others': []  # Para arquivos que não se encaixam em outras categorias
    }

    # Itera sobre os arquivos na pasta fornecida
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        # Pular diretórios
        if os.path.isdir(item_path):
            continue

        # Obter a extensão do arquivo
        _, ext = os.path.splitext(item)
        ext = ext.lower()

        # Encontrar a pasta correspondente ao tipo de arquivo
        target_folder = None
        for folder, extensions in file_type_folders.items():
            if ext in extensions:
                target_folder = os.path.join(folder_path, folder)
                break
        
        # Se não encontrou uma pasta, use 'Others'
        if target_folder is None:
            target_folder = os.path.join(folder_path, 'Others')

        create_folder(target_folder)
        shutil.move(item_path, os.path.join(target_folder, item))

    print("A pasta foi organizada!")

# Solicita o caminho da pasta ao usuário
folder_path = input("Digite o caminho da pasta a ser organizada: ").strip()

# Verifica se o caminho existe e se é uma pasta
if os.path.exists(folder_path) and os.path.isdir(folder_path):
    organize_files(folder_path)
else:
    print("O caminho fornecido não é válido. Verifique e tente novamente.")
