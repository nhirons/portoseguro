import re

# Data labels

def isInd(name):
    match = re.search('^.*ind.*$',name)
    if match:
        return True
    else:
        return False

def isReg(name):
    match = re.search('^.*reg.*$',name)
    if match:
        return True
    else:
        return False
    
def isCar(name):
    match = re.search('^.*car.*$',name)
    if match:
        return True
    else:
        return False

def isCalc(name):
    match = re.search('^.*calc.*$',name)
    if match:
        return True
    else:
        return False

# Data types

def isCat(name):
    match = re.search('^.*cat.*$',name)
    if match:
        return True
    else:
        return False

def isBin(name):
    match = re.search('^.*bin.*$',name)
    if match:
        return True
    else:
        return False
    
def notBinOrCat(name):
    match = re.search('^.*bin.*$',name)
    if match:
        return False
    else:
        match = re.search('^.*cat.*$',name)
        if match:
            return False
        else:
            return True

# Parsers

def label_parser(columns):

    label_dict = {}

    label_dict['ind'] = [col for col in columns if isInd(col)]
    label_dict['reg'] = [col for col in columns if isReg(col)]
    label_dict['car'] = [col for col in columns if isCar(col)]
    label_dict['calc'] = [col for col in columns if isCalc(col)]

    return label_dict

def type_parser(columns):

    type_dict = {}

    type_dict['cat'] = [col for col in columns if isCat(col)]
    type_dict['bin'] = [col for col in columns if isBin(col)]
    type_dict['con'] = [col for col in columns if notBinOrCat(col)]

    return type_dict

def total_parser(columns):

    column_labels = ['ind', 'reg', 'car', 'calc']
    column_types = ['cat', 'bin', 'con']
    
    parsed_labels = label_parser(columns)
    parsed_types = type_parser(columns)

    parsed_dict = {}

    for label in column_labels:
        parsed_dict[label] = {}

        for col_type in column_types:
            parsed_dict[label][col_type] = \
            [col for col in columns if \
            col in parsed_labels[label] and \
            col in parsed_types[col_type]]

    return parsed_dict