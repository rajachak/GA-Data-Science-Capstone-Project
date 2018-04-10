def preprocess (strng):
import re
    replace_list = ['peeled', 'fresh', 'ground', 'chopped', 'seeds', 'frozen',
                    'plain', 'light','heavy','dark', 'roasted', 'diced','cooked',
                    'pitted', 'canned', 'unsweeetened', 'sweetened', 'low',
                    'reduced','sodium','skim', 'part-skim', 'whole', 'low-fat',
                    'extra', 'extra-virgin','leaves', 'leaf', 'leaves','crumbles',
                    'powder','yellow', 'kosher', 'boneless', 'skinless', 'grilled',
                    'shredded', 'peeled', 'coarse', 'reduced', 'all-purpose', 'red',
                    'white', 'oven-ready', 'reduced-fat', 'thread', 'dried', 'dry',
                    'fat', 'free', 'finely', 'firmly', 'freshly', '1%', '2%', 'for',
                    'dusting', 'seasoned', 'sliced', 'slivered', 'soft', 'softened',
                    'small', 'toasted', 'unsweetened', 'pod', 'pods','cube','granule',
                    'floret','fine', 'baby', 'lower', 'lump', 'halves', 'lowfat',
                    'slices', 'all', 'purpose', 'unbleached', 'bone-in', 'granule',
                    'whole-milk', 'asian', 'sprigs', 'stem', 'cubes', 'granules', 'in',
                    'crumbled', 'crushed', 'blend', 'boneless', 'bottled', 'florets',
                    'california', 'chunky', 'flavored', 'cooking', 'baked', 'thai',
                    'store', 'bought', 'steamed', 'stewed', 'unsalted', 'unflavored',
                    'vietnamese', 'organic', 'cap', 'concentrate', 'packed', 'boiling',
                    'deveined', 'fat-free', 'self', 'rising', 'self-rising', 'instant',
                    'of', 'grated'
                   ]
    return_strng = ''
    strng = strng.lower()
    for w in strng.split():
        if w in replace_list:
            w = ''
        else:
            w = re.sub('oes$', 'o', w)
            w = re.sub('s$', '', w)           
        return_strng += w + ' '
        
    return_strng = re.sub('"', '', return_strng)
    return_strng = re.sub(',', '', return_strng)
    return_strng = re.sub('chilie', 'chile', return_strng)
    return_strng = re.sub('chillie', 'chile', return_strng)
    return_strng = re.sub('yoghurt', 'yogurt', return_strng)
    return_strng = re.sub('won ton ', 'wonton', return_strng)
    return_strng = re.sub('whipping', 'whipped', return_strng)
    return_strng = re.sub('anchovie', 'anchovy', return_strng)
    return_strng = re.sub('artichok heart marin', 'artichoke heart', return_strng)
    return_strng = re.sub('colouring', 'coloring', return_strng)
    return_strng = re.sub('hellmann\' or best food real mayonnai', 'mayonaise', return_strng)
    return_strng = re.sub('mayonnaise', 'mayonaise', return_strng)
    return_strng = re.sub('wontonwrapper', 'wonton wrapper', return_strng)
    return_strng = re.sub('filet', 'fillet', return_strng) 
    return_strng = re.sub('-', ' ', return_strng) 
    return_strng = return_strng.strip()
    return_strng = re.sub('  ', ' ', return_strng)
    return(return_strng)