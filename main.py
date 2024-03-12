from flask import Flask
from Source.settings_manager import settings_manager
from Source.Storage.storage import storage
from Source.errors import error_proxy
from Source.Logic.reporting_factory import report_factory
from Source.Logic.start_factory import start_factory

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

options = settings_manager()
start = start_factory(options.settings)
start.create()


@app.route("/api/report/<storage_key>", methods=["GET"])
def get_report(storage_key: str):
    keys = storage.storage_keys(start.storage)
    if storage_key == "" or storage_key not in keys:
        return error_proxy.create_error_response(app, f"Некорректный передан запрос! Необходимо передать: /api/report/<storage_key>: {keys}.", 400)

    report = report_factory()
    data = start.storage.data

    try:
        result = report.create_response(options.settings.report_mode, data, storage_key, app)
        return result
    except Exception as ex:
        return error_proxy.create_error_response(app, f"Ошибка при формировании отчета {ex}", 500)


if __name__ == "__main__":
    app.run(debug=True)