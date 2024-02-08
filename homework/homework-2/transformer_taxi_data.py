if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    data.columns = (data.columns
                    .str.replace(' ', '_')
                    .str.lower()
                    )
    return data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0) ]

