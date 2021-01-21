from datetime import datetime
import requests

class Convertor(object): 
    rates = {}  
    def __init__(self, url): 
        data = requests.get(url).json() 
        self.rates = data["rates"]  
  
    def convert_from_usd(self, amount_usd, to_currency):
        """
        Converts given USD amount into the 'to_currency' amount.
        """
        # Extracting only the rates from the json data 
        amount = amount_usd / self.rates['USD'] 
        if to_currency == 'USD':
            return amount_usd
        else:
            # limiting the precision to 2 decimal places 
            amount = round(amount * self.rates[to_currency], 2) 
            return amount


def get_campaign_duration(deadline, launched):
    """
    Returns duration of campaign based on launched date and deadline date.
    """
    deadline = datetime.strptime(deadline, '%Y-%m-%d').date()
    launched = datetime.strptime(launched, '%Y-%m-%d %H:%M:%S').date()
    return (deadline-launched).days

def get_year(date):
    """
    Returns year of the given date.
    """
    return datetime.strptime(date, '%Y-%m-%d %H:%M:%S').year

def plot_stack_bar_chart(success_cat, failed_cat, title, xlable, ylable):
    """
    Plots stacked bar chart.
    """
    annotations = []
    main_colors = dict(
        {'failed': 'rgb(300,50,50)', 
         'successful': 'rgb(50,300,50)'
        }
    )

    bar_success = go.Bar(
            x=success_cat.index,
            y=success_cat,
            name='successful',
        )

    bar_failed = go.Bar(
            x=failed_cat.index,
            y=failed_cat,
            name='failed',
        )

    data = [bar_success, bar_failed]
    layout = go.Layout(
        barmode='stack',
        autosize=False,
        width=800,
        height=400,
        annotations=annotations
    )

    fig = go.Figure(data=data, layout=layout)
    fig.update_layout(
    title=title,
    xaxis_title=xlable,
    yaxis_title=ylable
    )
    py.iplot(fig, filename='main_cat')
