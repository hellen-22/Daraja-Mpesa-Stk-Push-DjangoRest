# Daraja-Mpesa-Stk-Push-DjangoRest
Simple Mpesa Express Project that enables sending stk push and generating callback data.
Available endpoints:

```sql
/stk/
 ```
This endpoint allows sending stk push to the provided phone number. The required data for this POST request is phone number and amount.

```sql
/callback/
 ```
This endpoint allows viewing of callback data sent from Safaricom.
