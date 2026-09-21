"""Build index.html (single self-contained file) and, with --hosted, a hosted/ folder that keeps images as real files
so loading="lazy" saves bytes. Usage: python build.py [--hosted]"""
import base64, re, sys, shutil, os
MIME = {'jpg': 'image/jpeg', 'png': 'image/png', 'webp': 'image/webp'}
EXT = r'(?:jpg|png|webp)'
def data(path):
    return 'data:' + MIME[path.rsplit('.', 1)[1]] + ';base64,' + base64.b64encode(open(path, 'rb').read()).decode()

html = open('index.src.html', encoding='utf8').read()
css = open('styles.css', encoding='utf8').read()

if '--hosted' in sys.argv:
    os.makedirs('hosted/assets', exist_ok=True)
    for f in os.listdir('assets'):
        shutil.copy('assets/' + f, 'hosted/assets/' + f)
    out = html.replace('<link rel="stylesheet" href="styles.css">', '<style>\n' + css + '\n</style>')
    open('hosted/index.html', 'w', encoding='utf8').write(out)
    print('hosted/index.html', len(out) // 1024, 'KB + assets/')
else:
    css = re.sub(r'url\("(assets/[^"]+)"\)', lambda m: 'url("' + data(m.group(1)) + '")', css)
    html = html.replace('<link rel="stylesheet" href="styles.css">', '<style>\n' + css + '\n</style>')
    html = re.sub(r'src="(assets/[^"]+\.' + EXT + r')"', lambda m: 'src="' + data(m.group(1)) + '"', html)
    open('index.html', 'w', encoding='utf8').write(html)
    print(len(html) // 1024, 'KB')
