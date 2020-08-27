import argparse
import pathlib

import touchy
import feely

def tf_score(a,b):
    if a == 0 and b == 0:
        return 0
    else:
        return (a-b)/(a+b)


if __name__ == "__main__":
    print("Touchy Feeling...")
    parser = argparse.ArgumentParser(
        description="Touchy Feely analysis of your feelings about your code"
    )
    parser.add_argument("path", help="path to begin Touchy Feely analysis")
    parser.add_argument("--recursive", help="No to analyse as a whole or Yes to do module-wise", action='store_true')
    args = parser.parse_args()

    if not args.recursive:
        module = touchy.ModuleToucher(args.path)
        module.touch()
        feelings = feely.Feeler("\n".join(module.texts_in_module))
        feelings.feel()
        score = tf_score(feelings.feeling["pos"], feelings.feeling["neg"])
        print(f'Feelings for "{module.module_name}" are: {feelings.feeling} with TF-score {score}')
    else:
        for mod in [mod for mod in pathlib.Path(args.path).glob("*") if mod.is_dir() and ".git" not in mod.name]:
            module = touchy.ModuleToucher(mod)
            module.touch()
            feelings = feely.Feeler("\n".join(module.texts_in_module))
            feelings.feel()
            score = tf_score(feelings.feeling["pos"], feelings.feeling["neg"])
            print(f'Feelings for "{mod.name}" are: {feelings.feeling} with TF-score {score}')
