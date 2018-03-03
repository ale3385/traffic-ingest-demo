from __future__ import print_function, absolute_import
from datetime import datetime, timedelta
import logging
from flask import Flask, request
from google.cloud import bigquery
import ingest.socrata_data as socrata_data

app = Flask(__name__)

@app.route('/traffic-ingest-demo/socrata-data') 
def start_traffic_add_data(): 
    is_cron = request.headers.get('X-Appengine-Cron', False)
    if not is_cron:
        return 'Bad Request', 400

    try:
        socrata_data.run()
        return "Pipeline started", 200
    except Exception as e:
        logging.exception(e)
        return "Error: <pre>{}</pre>".format(e), 500
        
@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)