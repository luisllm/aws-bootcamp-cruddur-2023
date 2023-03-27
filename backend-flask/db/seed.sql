-- this file was manually created
INSERT INTO public.users (display_name, handle, email, cognito_user_id)
VALUES 
  ('Andrew Brown', 'andrewbrown' , 'andrewbrown@example.co' , 'MOCK'),
  ('Andrew Bayko', 'bayko' , 'bayko@example.co' , 'MOCK'),
  ('Luis Longo','llm', 'luis.longo.m@gmail.com', 'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'llm' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )