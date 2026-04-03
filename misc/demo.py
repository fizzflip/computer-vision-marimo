import marimo

__generated_with = "0.19.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import math
    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # 🔍 Interactive Search & Answer Demo (marimo)

    Type a question or keyword below.
    The app searches a small knowledge base and returns:
    - ranked results
    - a synthesized answer

    This notebook runs **standalone in a browser** using marimo.
    """)
    return


@app.cell
def _(mo):
    query = mo.ui.text(
        label="Search query",
        placeholder="e.g. What is marimo?",
    )
    query
    return (query,)


@app.cell
def _():
    # A tiny local "knowledge base"
    DOCUMENTS = {
        "marimo": "Marimo is a reactive Python notebook designed for building interactive data apps that run in the browser.",
        "python": "Python is a high-level programming language known for readability and a rich ecosystem.",
        "notebook": "A notebook combines executable code, text, and visuals into a single interactive document.",
        "browser": "Modern browsers can host interactive applications using local servers or WebAssembly.",
        "search": "Search systems retrieve relevant documents based on a user query.",
    }
    DOCUMENTS
    return (DOCUMENTS,)


@app.cell
def _(DOCUMENTS, mo, query):
    def score(text, q):
        if not q:
            return 0
        q = q.lower()
        text = text.lower()
        return sum(1 for w in q.split() if w in text)

    q = query.value.strip()

    ranked = sorted(
        DOCUMENTS.items(),
        key=lambda kv: score(kv[1], q),
        reverse=True,
    )

    results = [(k, v) for k, v in ranked if score(v, q) > 0]

    if not q:
        mo.callout("Enter a query to search.", kind="info")
        mo.stop(1)

    if not results:
        mo.callout("No results found.", kind="warning")
        mo.stop(1)

    mo.md("## 📄 Search Results")
    for title, text in results:
        mo.md(f"**{title.capitalize()}** — {text}")

    answer = results[0][1]

    mo.md("## 🤖 Answer")
    mo.callout(answer, kind="success")
    return


@app.cell
def _(mo):
    import urllib.request

    url = "https://w.wallhaven.cc/full/9o/wallhaven-9oo8k1.jpg"

    with urllib.request.urlopen(url) as r:
        image_bytes = r.read()

    mo.image(image_bytes)
    return


if __name__ == "__main__":
    app.run()
