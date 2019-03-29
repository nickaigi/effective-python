class LazyDB(object):
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = 'Value for %s' % name
        setattr(self, name, value)
        return value


class LoggingLazyDB(LazyDB):
    def __getattr__(self, name):
        print('Called __getattr__(%s)' % name)
        return super().__getattr__(name)


class ValidationDB(object):
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        try:
            return super().__getattribute__(name)
        except AttributeError:
            value = 'Value for %s' % name
            setattr(self, name, value)
            return value


class MissingPropertyDB(object):
    def __getattr__(self, name):
        if name == 'bad_name':
            raise AttributeError('%s is missing' % name)
        value = 'value for %s' % name
        setattr(self, name, value)
        return value


class SavingDB(object):
    def __setattr__(self, name, value):
        # save some data to the DB log
        super().__setattr__(name, value)


class LoggingSavingDB(SavingDB):
    def __setattr__(self, name, value):
        print('Called __setattr__(%s, %r)' % (name, value))
        super().__setattr__(name, value)


class BrokenDictionaryDB(object):
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        # python will recurse until it reaches its stack limit, then it will die
        return self._data[name]


class DictionaryDB(object):
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, name):
        data_dict = super().__getattribute__('_data')
        return data_dict[name]


def main():
    # data = LazyDB()
    # print('Before:', data.__dict__)
    # print('foo:   ', data.foo)
    # print('After: ', data.__dict__)
    
    # data = LoggingLazyDB()
    # print('exists:', data.exists)
    # print('foo:   ', data.foo)
    # print('foo:   ', data.foo)

    # data = ValidationDB()
    # print('exists:', data.exists)
    # print('foo:   ', data.foo)
    # print('foo:   ', data.foo)

    # data = MissingPropertyDB()
    # data.bad_name

    # data = LoggingLazyDB()
    # print('Before:     ', data.__dict__)
    # print('foo exists: ', hasattr(data, 'foo'))
    # print('After:      ', data.__dict__)
    # print('foo exists: ', hasattr(data, 'foo'))

    # data = LoggingSavingDB()
    # print('Before:  ', data.__dict__)
    # data.foo = 5
    # print('After:   ', data.__dict__)
    # data.foo = 7
    # print('Finally: ', data.__dict__)

    # try:
    #     data = BrokenDictionaryDB({'foo': 3})
    #     data.foo
    # except:
    #     print('Excpected exception')

    data = DictionaryDB({'foo': 3})
    print(data.foo)


if __name__ == '__main__':
    main()
