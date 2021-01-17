

#读取yaml
import yaml


class Yml():


    def yml(self):

        f=open('demo1.yaml')
        data=yaml.load(f.read())

        return data

if __name__ == '__main__':

    A=  Yml().yml()
    print(A['people']['age'])