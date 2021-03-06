# Do I need this or is it covered by _output_file_check.py ?
import config
import collections
base = "/* Output:"

if __name__ == '__main__':
    all = collections.defaultdict(list)
    for java in config.example_dir.rglob("*.java"):
        text = java.read_text()
        for line in text.splitlines():
            if(line.startswith(base)):
                all[line.strip()].append((java, text))

    for k in sorted(all.keys()):
        if(k != base):
            print(k)
            for tup in all[k]:
                rel = tup[0].relative_to(config.example_dir)
                print("\t" + str(rel))

    vbh = [tup for tup in all[k] for k in all.keys() if "{VisuallyInspectOutput}" in tup[1]]
    if vbh:
        print("=" * 50)
        print("{VisuallyInspectOutput} + /* Output:")
        for tup in vbh:
            rel = tup[0].relative_to(config.example_dir)
            print(str(rel))
