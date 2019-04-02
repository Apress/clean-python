def awesome_attr(future_class_name, future_class_parents, future_class_attr):
    """
      Return a class object, with the list of its attribute prefix with awesome keyword.
    """
    # pick any attribute that doesn't start with '__' and prefix with awesome
    awesome_prefix = {}
    for name, val in future_class_attr.items():
        if not name.startswith('__'):
            uppercase_attr["_".join("awesome", name)] = val
        else:
            uppercase_attr[name] = val

    # let `type` do the class creation
    return type(future_class_name, future_class_parents, uppercase_attr)


__metaclass__ = uppercase_attr # this will affect all classes in the module


class Example: # global __metaclass__ won't work with "object" though
    # but we can define __metaclass__ here instead to affect only this class
    # and this will work with "object" children
    val = 'yes'
