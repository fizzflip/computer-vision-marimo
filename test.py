import marimo

__generated_with = "0.19.6"
app = marimo.App(width="medium", auto_download=["ipynb", "html"])


@app.cell
def _():
    import oracledb
    return (oracledb,)


@app.cell
def _(oracledb):
    connection = oracledb.connect(user="SYSTEM", password="pass123", dsn="localhost/freepdb1")
    print("Successfully connected to Oracle Database")
    return (connection,)


@app.cell
def _(connection):
    connection.is_healthy()
    return


@app.cell
def _(connection, mo):
    _df = mo.sql(
        f"""
        CREATE TABLE students(sid NUMBER(14), first_name VARCHAR(10), last_name VARCHAR(10), email VARCHAR(10));
        """,
        engine=connection
    )
    return


@app.cell
def _(connection, mo, students):
    _df = mo.sql(
        f"""
        INSERT INTO students VALUES (1, "Raj", "Shamani", "rajshamani");
        """,
        engine=connection
    )
    return


@app.cell
def _(connection, mo, students):
    _df = mo.sql(
        f"""
        SELECT * FROM students
        """,
        engine=connection
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
