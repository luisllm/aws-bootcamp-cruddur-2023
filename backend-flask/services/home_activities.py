from datetime import datetime, timedelta, timezone
from opentelemetry import trace
import logging


from lib.db import pool, query_wrap_array



tracer = trace.get_tracer("home.activities")

class HomeActivities:
  def run(logger, cognito_user_id=None):
    logger.info("HomeActivities")
    with tracer.start_as_current_span("home-activities-mock-data"):
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())

      sql = query_wrap_array("""
      SELECT
        activities.uuid,
        users.display_name,
        users.handle,
        activities.message,
        activities.replies_count,
        activities.reposts_count,
        activities.likes_count,
        activities.reply_to_activity_uuid,
        activities.expires_at,
        activities.created_at
      FROM public.activities
      LEFT JOIN public.users ON users.uuid = activities.user_uuid
      ORDER BY activities.created_at DESC
      """)
      print("SQL-------------------")
      print(sql)
      print("SQL-------------------")

      with pool.connection() as conn:
        with conn.cursor() as cur:
          cur.execute(sql)
          # this will return a tuple
          # the first field being the data
          json = cur.fetchone()
      print("HERE-------------")
      print(json[0])
      return json[0]


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
      
      
      return results