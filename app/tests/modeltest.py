
from models import Quote
import unittest

class TestQuote(unittest.TestCase):
    def setUp(self):
        self.new_quote=Quote(
            "Henry Petroski",
            35,
            "The most amazing achievement of the computer software industry is its continuing cancellation of the steady and staggering gains made by the computer hardware industry.",
            "http://quotes.stormconsultancy.co.uk/quotes/35"
        )
        self.assertIsInstance(Quote)

if __name__=='__main__':
    unittest.main()