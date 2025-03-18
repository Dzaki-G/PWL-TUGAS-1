# Django E-commerce Microservices

This is a microservices-based Django e-commerce platform with the following services:
1. **Cart Service** - Manages the shopping cart.
2. **Order Service** - Manages orders.
3. **Coupons Service** - Manages coupons and discounts.
4. **Shop Service** - Manages products and product catalog.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Django-ecommerce-microservices.git
    cd Django-ecommerce-microservices
    ```

2. Set up each service (Cart, Order, Coupons, Shop) individually:
    - For each service, create a virtual environment:
      ```bash
      python -m venv venv
      source venv/bin/activate
      ```

    - Install dependencies:
      ```bash
      pip install -r requirements.txt
      ```

    - Run migrations for each service:
      ```bash
      python manage.py migrate
      ```

3. Ensure that you have MySQL databases set up:
    - `cart_db`
    - `order_db`
    - `coupons_db`
    - `shop_db`

4. Run each service:
    ```bash
    python manage.py runserver
    ```

5. Use the API Gateway (Nginx) to route requests to the appropriate service.
