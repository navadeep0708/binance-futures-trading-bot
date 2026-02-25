import logging
from binance.exceptions import BinanceAPIException, BinanceOrderException


def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(
            f"Placing order: Symbol={symbol}, Side={side}, "
            f"Type={order_type}, Quantity={quantity}, Price={price}"
        )

        
        try:
            client.futures_change_leverage(symbol=symbol, leverage=10)
            logging.info(f"Leverage set to 10x for {symbol}")
        except Exception as leverage_error:
            logging.warning(f"Leverage setting skipped: {leverage_error}")

        # Place Order 
        if order_type == "MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logging.info(f"Market Order Response: {response}")
            return response

        elif order_type == "LIMIT":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            logging.info(f"Initial Limit Order Response: {response}")

            # Fetch updated order for LIMIT
            order_id = response["orderId"]

            updated_order = client.futures_get_order(
                symbol=symbol,
                orderId=order_id
            )

            logging.info(f"Final Limit Order Status: {updated_order}")
            return updated_order

        else:
            raise ValueError("Unsupported order type")

    except BinanceAPIException as e:
        logging.error(f"Binance API Error: {e.message}")
        raise Exception(f"Binance API Error: {e.message}")

    except BinanceOrderException as e:
        logging.error(f"Binance Order Error: {e.message}")
        raise Exception(f"Binance Order Error: {e.message}")

    except Exception as e:
        logging.error(f"Unexpected Error: {str(e)}")
        raise Exception(f"Unexpected Error: {str(e)}")