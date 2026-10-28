from pathlib import Path
import shutil


ASSIGNMENT_DIR = Path(__file__).resolve().parent
DEMO_DIR = ASSIGNMENT_DIR / "organizer-demo"
INCOMING_DIR = DEMO_DIR / "incoming"
ORGANIZED_DIR = DEMO_DIR / "organized"


def create_demo_files():
    if INCOMING_DIR.exists():
        return

    INCOMING_DIR.mkdir(parents=True)
    examples = {
        "notes.txt": "Practice organizing files with Python.\n",
        "report.csv": "name,score\nAda,95\n",
        "script.py": "print('Hello, files!')\n",
        "photo.jpg": "Example image placeholder.\n",
        "README": "This example file has no extension.\n",
    }

    for filename, content in examples.items():
        (INCOMING_DIR / filename).write_text(content, encoding="utf-8")


def list_incoming_files() -> list[Path]:
    # TODO: Retorne somente os arquivos diretamente dentro de INCOMING_DIR.
    raise NotImplementedError


def group_by_extension(files: list[Path]) -> dict[str, list[Path]]:
    # TODO: Agrupe os arquivos pela extensão normalizada.
    # Use "sem-extensao" quando um arquivo não tiver extensão.
    raise NotImplementedError


def organize_files(groups: dict[str, list[Path]]) -> int:
    # TODO: Crie as pastas de destino e mova os arquivos sem sobrescrever arquivos existentes.
    # Retorne a quantidade de arquivos movidos.
    raise NotImplementedError


def main():
    create_demo_files()
    files = list_incoming_files()
    groups = group_by_extension(files)

    print("Prévia da organização:")
    for extension, grouped_files in groups.items():
        names = ", ".join(file.name for file in grouped_files)
        print(f"{extension}: {names}")

    organized_count = organize_files(groups)
    print(f"Arquivos organizados: {organized_count}")


if __name__ == "__main__":
    main()