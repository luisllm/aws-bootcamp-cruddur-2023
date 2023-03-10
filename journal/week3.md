# Week 3 — Decentralized Authentication
## My journal - week3

-  **Did all the tasks in the week3 to-do list**
   -  **Custom Signup page**
![image week3-signup1](./images/week3-signup1.png)
&nbsp;
![image week3-signup2](./images/week3-signup2.png)
&nbsp;
![image week3-signup2](./images/week3-signup3.png)

   -  **Custom Confirmation page**
![image week3-confirmation1](./images/week3-confirmation1.png)
&nbsp;
![image week3-confirmation2](./images/week3-confirmation2.png)

   -  **Custom Signin page**
![image week3-signin1](./images/week3-signin1.png)
&nbsp;
![image week3-signin2](./images/week3-signin2.png)

   -  **Verified JWT Token server side to serve authenticated API endpoints in Flask Application**
![image week3-backend-jwt1](./images/week3-backend-jwt1.png)
&nbsp;
In home_activities.py:
&nbsp;
```
      if cognito_user_id != None:
        extra_crud= {
          'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
          'handle':  'Lore',
          'message': 'This is for auth users only',
          'created_at': (now - timedelta(hours=1)).isoformat(),
          'expires_at': (now + timedelta(hours=12)).isoformat(),
          'likes': 1000,
          'replies': []
        }
        results.insert(0,extra_crud)

      span.set_attribute("app.result_length", len(results))
      return results
```
&nbsp;
![image week3-backend-jwt2](./images/week3-backend-jwt2.png)