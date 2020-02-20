# -*- coding: utf-8 -*-

def addId(numerateur, denominateur):
    """
    Effectue une division

    :param numerateur: le numerateur de la division
    :type numerateur: int
    :param denominateur: le denominateur de la division
    :type denominateur: int
    :return: la valeur entiere de la division
    :rtype: int
    """

    if denominateur == 0:
        print('denominateur interdit')
    else:
        result = int(numerateur)/int(denominateur)
        return result

if __name__ == '__main__':
    print(ma_fonction_simple(4,2))