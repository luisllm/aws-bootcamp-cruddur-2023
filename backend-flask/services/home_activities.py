from datetime import datetime, timedelta, timezone
from opentelemetry import trace
import logging


from lib.db import db



tracer = trace.get_tracer("home.activities")

class HomeActivities:
  def run(cognito_user_id=None):
    #logger.info("HomeActivities")
    with tracer.start_as_current_span("home-activities-mock-data"):
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
      sql = db.template('activities','home')
      results = db.query_array_json(sql)
      return results


      #if cognito_user_id != None:
      #  extra_crud= {
      #    'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
      #    'handle':  'Lore',
      #    'message': 'This is for auth users only',
      #    'created_at': (now - timedelta(hours=1)).isoformat(),
      #    'expires_at': (now + timedelta(hours=12)).isoformat(),
      #    'likes': 1000,
      #    'replies': []
      #  }
      #  results.insert(0,extra_crud)

      #span.set_attribute("app.result_length", len(results))
      
      