from btc.models import Price
from bitcoin_rnn.models import FuturePrice
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.models import load_model
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Loading model...')
        model = load_model('bitcoin_rnn_model.h5')
        self.stdout.write(self.style.SUCCESS('Model loaded!'))

    
