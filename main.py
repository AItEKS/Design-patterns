from Source.Logic.reporting_factory import report_factory
from Source.exceptions import operation_exception
from flask import Flask, request

app = Flask(__name__)
report_generator = report_factory()


@app.route("/api/report/<storage_key>", methods=["GET"])
def get_report(storage_key):
    data = {}
    format = request.args.get('format')
    if format is None:
        raise operation_exception("Не указан формат отчета")

    try:
        return report_generator.create(format, data)
    except operation_exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True)
