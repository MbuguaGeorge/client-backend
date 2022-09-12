## API Endpoints

To test the following endpoints use **Postman** or **CURL**  
Pass form data as key-value pairs in body. Auth credentials to be passed in header as: `Auhorization: Token <access_token>`

- **POST** `/profile/register`
Creates new user
- **POST** `/profile/validate`
Validates user email
- **POST** `/profile/login`
Authenticates a user
- **PUT** `/profile/update`
Updates user profile
- **GET** `/profile/cur`
Returns current logged in user
- **POST** `/orders/summary`
Creates an order
- **PUT** `/dashboard/status/pk`
Change status of an order (Recent, Canceled, Finished)
- **GET** `/dashboard/list`
Lists recent orders
- **GET** `/dashboard/canceled`
Lists canceled orders
- **GET** `/dashboard/finished`
Lists finished orders
- **GET** `/dashboard/recent/pk`
Returns details of an order
- **POST** `/card/receive-payment`
Pay for an order
