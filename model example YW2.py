from functools import wraps


class Data(object):
    def __init__(self):
        self.logger = None
        self.settings = {}
        self.assets = []
        self.data = {}
        self.returns = {}
        self.risk = {}
        self.signal = {}
        self.portfolio = {}


class Logger(object):
    # Different levels of results logging, such as INFO, DEBUG, WARN, ERROR
    pass

class Plotter(object):
    pass


def parse_bt_date(settings):
    pass

def cache_check():
    def wrap(func):
        @wraps(func)
        def _g(self):
            # check cache
            pass

        return _g

    return wrap


class Model(Data):
    def __init__(self, name, settings):
        Data.__init__(self)

        self.logger = Logger(settings)
        (self.st_dt, self.to_dt) = parse_bt_date(settings)
        self.settings = self.compile_settings(settings, name)
        self.factors = self.get_factors(settings, name)
        self.name = name
        self.plotter = Plotter()

    def run(self):
        self.collect_data()
        self.calculate_returns()
        self.calculate_risk()
        self.calculate_signals()
        self.calculate_nv_portfolio()
        self.calculate_op_portfolio()
        self.calculate_btstats()
        self.plot()

    @cache_check()
    def collect_data(self):
        # TODO: init DBReader, init traded assets, collect raw data
        # self.data = dict(res)
        pass

    @cache_check()
    def calculate_returns(self):
        # TODO: generic function based on prices and TRI, settlement returns and in-out returns can both be loaded
        # self.ret = dict(res)
        pass

    @cache_check()
    def calculate_risk(self):
        # TODO: standard risk output, var, corr, beta
        # self.risk = dict(res)
        pass

    @cache_check()
    def calculate_signals(self):
        # TODO: loop over signals (factors), within each factor, the same functions sequence run (factor.run) can be
        #  used.
        self.check_model_allocations()
        #### loop over factors, it can use the preloaded self.data, self.ret, self.risk
        for factor in self.factors:
            factor.run()
        # self.signal = dict(res)

    @cache_check()
    def calculate_nv_portfolio(self):
        # TODO: Naive Portfolio, Analytical Optimal, Signal Aggregation
        # self.nv_portfolio = dict(res)
        pass

    @cache_check()
    def calculate_op_portfolio(self):
        # TODO: Numerical Layer of Optimization
        # self.op_portfolio = dict(res)
        pass

    @cache_check()
    def calculate_btstats(self):
        # TODO: Key stats and output from the model
        # self.bt_stats = dict(res)
        pass

    def plot(self):
        # TODO: Standard Model Plots
        # it can use all output from previous steps for any meaningful plots
        pass

    def compile_settings(self, settings, name):
        return settings

    def get_factors(self, settings, name):
        pass

    def check_model_allocations(self):
        pass


class Factor(Model):
    def __init__(self, name, settings):
        super().__init__(settings, name)
        self.name = name

    def run(self):
        # pure computation of signal based on self.data, self.ret, self.risk.
        # the core part of the signal calc does not have to be sequential function calls
        pass
