-- this file was manually created
INSERT INTO public.users (display_name, handle, email, cognito_user_id)
VALUES 
  ('Andrew Brown', 'andrewbrown' , 'andrewbrown@example.co' , 'MOCK'),
  ('Andrew Bayko', 'bayko' , 'bayko@example.co' , 'MOCK'),
  ('Luis Longo','luis', 'luis.longo.m@gmail.com', 'MOCK'),
  ('pedro','pedro', 'luis.longo@nagra.com', 'MOCK'),
  ('Londo Mollari', 'londo' , 'lmollari@centari.co' , 'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'luis' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  ),
  (
    (SELECT uuid from public.users WHERE users.handle = 'pedro' LIMIT 1),
    'I am the other!',
    current_timestamp + interval '10 day'
  );