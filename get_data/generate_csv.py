import csv,os
from get_data.models import Dates, CryptoPairs, PeriodData, ExecutedTrades, OrderBookEntry



def get_models():
    all_dates = Dates.objects.all()
    data_set_return = []

    for date in all_dates:
        all_pairs = date.cryptopairs_set.all()

        for pair in all_pairs:
            period_data = pair.perioddata_set.all()

            for period_d in period_data:
                executed_trades = period_d.executedtrades_set.all()

                for trade in executed_trades:
                    data_row = ([date.date.strftime('%d/%m/%Y'),pair.pair,period_d.period,"{:.9f}".format(float(period_d.current_rate)),
                                "{:.9f}".format(float(period_d.bid_price)),"{:.9f}".format(float(period_d.ask_price)),
                                int(period_d.num_sell_orders),int(period_d.num_buy_orders),
                                "{:.10f}".format(float(period_d.val_sell_orders)),"{:.10f}".format(float(period_d.val_buy_orders)),
                                "{:.10f}".format(float(period_d.largest_sell_order_quantity)),"{:.10f}".format(float(period_d.largest_sell_order_value)),
                                "{:.10f}".format(float(period_d.largest_buy_order_quantity)),"{:.10f}".format(float(period_d.largest_buy_order_value)),
                                trade.order_id,trade.timestamp,"{:.9f}".format(float(trade.quantity)),"{:.9f}".format(float(trade.price)),
                                "{:.9f}".format(float(trade.total)),trade.fill_type,trade.order_type])

                    data_set_return.append(data_row)

    return data_set_return

def get_period_data_models():
    all_dates = Dates.objects.all()
    data_set_return = []

    for date in all_dates:
        all_pairs = date.cryptopairs_set.all()

        for pair in all_pairs:
            period_data = pair.perioddata_set.all()

            for period_d in period_data:
                data_row = ([pair.pair,period_d.period,
                            period_d.start_timestamp,"{:.9f}".format(float(period_d.bid_price)),
                            "{:.9f}".format(float(period_d.ask_price)),"{:.9f}".format(float(period_d.current_rate)),
                            "{:.9f}".format(float(period_d.ask_price)-float(period_d.bid_price))])
                data_set_return.append(data_row)
    return data_set_return

def write_file_csv(filename,data,header=None):
    # write data back to csv
    index = 0
    with open(filename,'w') as csvfile:
        csv_writer = csv.writer(csvfile) 
        if header:
            csv_writer.writerow(header)
        for row in data:
            csv_writer.writerow(row)
            index += 1
        print ("Rows : " + str(len(data)))
        print ("Writes: " + str(index))

def read_from_file_csv(filename):
    csv_data = []
    with open(filename,'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            try:
                if row[5] is '':
                    continue 
            except IndexError as e:
                pass
            csv_data.append(row)
    return csv_data


def gen_dataset(filename):
    # dataset = get_models()
    # header = (["date","pair","period","current_rate","bid","ask",
    #             "num_sell_orders","num_buy_orders","val_sell_orders","val_buy_orders",
    #             "largest_sell_order_quantity","largest_sell_order_value","largest_buy_order_quantity",
    #             "largest_buy_order_value","trade_id","trade_timestamp","trade_quantity","trade_price",
    #             "trade_total","trade_fill_type","trade_order_type"])
    # write_file_csv("get_data/datasets/ABTC-LTC-5mins.csv",dataset,header)
    dataset = get_period_data_models()
    header = ["pair","period","timestamp","bid","ask","current_rate","spread"]
    spreads = [d[6] for d in dataset][1:]
    write_file_csv("get_data/datasets/"+filename+".csv",dataset,header)
