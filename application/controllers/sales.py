from datetime import datetime, timedelta

from application.models.database import Firestore

class Sales:

    def __init__(self):
        self.database = Firestore()

    def insert_sale(self, sale_data):

        response = self.database.insert_sale(sale_data)
        
        return response

    def get_sale(self, sale_id):

        response = self.database.get_sale(sale_id)

        return response

    def get_all_sales(self):

        response = self.database.get_all_sales()

        return response

    def get_all_week_sales(self):

        time_from = datetime.now() - timedelta(days=7)
        time_till = datetime.now()
        time_from_timestamp = datetime.timestamp(time_from)
        time_till_timestamp = datetime.timestamp(time_till)

        response = self.database.get_week_sales_by_timestamp(time_from_timestamp, time_till_timestamp)

        return response

    def get_past_three_week_sales(self):

        time_from = datetime.now() - timedelta(days=3)
        time_till = datetime.now()
        time_from_timestamp = datetime.timestamp(time_from)
        time_till_timestamp = datetime.timestamp(time_till)

        response = self.database.get_week_sales_by_timestamp(time_from_timestamp, time_till_timestamp)

        return response

    def update_sale(self, sale_data):

        response = self.database.update_sale(sale_data)

        return response

    def delete_sale(self, sale_id):

        response = self.database.delete_sale(sale_id)

        return response

    def get_percentages(self):
        
        response = self.database.get_percentages()

        return response

    def get_earnings(self):

        time_from = datetime.now() - timedelta(days=1)
        time_till = datetime.now()
        time_from_timestamp = datetime.timestamp(time_from)
        time_till_timestamp = datetime.timestamp(time_till)
        get_yesterday = self.database.get_week_sales_by_timestamp(time_from_timestamp, time_till_timestamp)

        week_sales = self.get_all_week_sales()
        last_three_sales = self.get_past_three_week_sales()

        week = round(sum([sale['sales_amount'] for sale in week_sales]), 2)
        last_three = round(sum([sale['sales_amount'] for sale in last_three_sales]), 2)
        yesterday = get_yesterday[0]['sales_amount'] if get_yesterday else 0

        response = {
            'week': week,
            'last_three_days': last_three,
            'yesterday': yesterday
        }

        return response