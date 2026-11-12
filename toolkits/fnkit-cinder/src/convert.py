import json
import pathlib


def convert(notebook_path, output_path):
    data = json.loads(pathlib.Path(notebook_path).read_text(encoding="utf-8"))
    cells = data.get("cells", [])
    lines = ["<!doctype html>", "<html><body>"]
    for cell in cells:
        if cell.get("cell_type") == "markdown":
            lines.append("<p>" + "".join(cell.get("source", [])) + "</p>")
    lines.append("</body></html>")
    pathlib.Path(output_path).write_text("\n".join(lines), encoding="utf-8")
    return len(cells)
