import argparse

import touchy
import feely


if __name__ == "__main__":
    print("Touchy Feeling...")
    parser = argparse.ArgumentParser(
        description="Touchy Feely analysis of your feelings about your code"
    )
    parser.add_argument("module_path", help="path to module")
    args = parser.parse_args()

    module = touchy.ModuleToucher(args.module_path)
    module.touch()
    print(module.texts_in_module)
