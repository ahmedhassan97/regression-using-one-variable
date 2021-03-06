{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "project1_linear_regression.py",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ahmedhassan97/regression-using-one-variable/blob/master/project1_linear_regression.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "beWJ_mhYz4Tb",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9T2WZXNx0NGO",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "path = 'data.csv'\n",
        "data = pd.read_csv(path, header=None, names=['Population',\n",
        "'Profit'])"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wiyxIUwl0iRv",
        "colab_type": "code",
        "outputId": "a4c50daa-81b5-4d42-bd10-2e8e02094402",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 759
        }
      },
      "source": [
        "#show data details\n",
        "print('data = \\n' ,data.head(10) )\n",
        "print('**************************************')\n",
        "print('data.describe = \\n',data.describe())\n",
        "print('**************************************')\n",
        "#draw data\n",
        "data.plot(kind='scatter', x='Population', y='Profit', figsize=(5,5))"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "data = \n",
            "    Population   Profit\n",
            "0      6.1101  17.5920\n",
            "1      5.5277   9.1302\n",
            "2      8.5186  13.6620\n",
            "3      7.0032  11.8540\n",
            "4      5.8598   6.8233\n",
            "5      8.3829  11.8860\n",
            "6      7.4764   4.3483\n",
            "7      8.5781  12.0000\n",
            "8      6.4862   6.5987\n",
            "9      5.0546   3.8166\n",
            "**************************************\n",
            "data.describe = \n",
            "        Population     Profit\n",
            "count   97.000000  97.000000\n",
            "mean     8.159800   5.839135\n",
            "std      3.869884   5.510262\n",
            "min      5.026900  -2.680700\n",
            "25%      5.707700   1.986900\n",
            "50%      6.589400   4.562300\n",
            "75%      8.578100   7.046700\n",
            "max     22.203000  24.147000\n",
            "**************************************\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7fbe1beca710>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 16
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAUkAAAE9CAYAAACGOZB/AAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjIsIGh0\ndHA6Ly9tYXRwbG90bGliLm9yZy8li6FKAAAgAElEQVR4nO3df5RcdZnn8ffTle5OSEISkhBDEow7\nwdkNTGi0lx8GOVHnKIIGXZQjjsKMrgxnYY+s4ySMHhTlzCg46LqKOlE4wsioSFQyyKwiPwbhaJwO\nhpAElcgipAkhtJikIel0Vz37R90KtytVt6q77q26devzOqfT1bdu1X3SVf3U873fH9fcHRERqayr\n1QGIiKSZkqSISAQlSRGRCEqSIiIRlCRFRCIoSYqIRJjS6gDqMW/ePF+6dGmrwxCRjNm0adPz7j4/\nap/EkqSZLQFuARYADqxz9y+a2dXAh4A9wa4fc/e7op5r6dKlDAwMJBWqiHQoM/t9rX2SrCTHgL9x\n94fNbCawyczuDu77grv/Y4LHFhGJRWJJ0t13AbuC2/vN7DFgUVLHExFJQlM6bsxsKXAKsDHYdLmZ\nbTGzm8xsTjNiEBGZjMSTpJnNANYDV7j7PuCrwJ8AfRQrzeurPO4SMxsws4E9e/ZU2kVEJHGJJkkz\n66aYIG919+8DuPtud8+7ewH4OnBqpce6+zp373f3/vnzIzufREQSk1iSNDMDbgQec/fPh7YvDO32\nTmBrUjGIiDQqyd7tlcD7gUfNbHOw7WPAhWbWR3FY0JPAXycYg4hIQ5Ls3X4QsAp3RY6JFBGZqKHh\nEXa+cIDFc6Yxd0ZvrM/dFjNuRESquWPzIGvXb6G7q4vRQoHrzl/B6r74Rhtq7raItK2h4RHWrt/C\nwdEC+0fGODhaYM36LQwNj8R2DCVJEWlbO184QHfX+DTW3dXFzhcOxHYMJUkRaVuL50xjtFAYt220\nUGDxnGmxHUNJUkTa1twZvVx3/gqmdncxs3cKU7u7uO78FbF23qjjRkTa2uq+RaxcNk+92yIi1cyd\n0Rt7cixRc1tEJIKSpIhIBCVJEZEISpIiIhGUJEVEIihJiohEUJIUEYaGR3jk6T/GOuc5KzROUqTD\nJb2KTrtTJSnSwZqxik67U5IU6WDNWEWn3SlJinSwZqyi0+6UJEU6WDNW0Wl36rgR6XBJr6LT7pQk\nRSTRVXTanZrbIhK7LI27VCUpIrHK2rhLVZIiEpssjrtUkhSR2GRx3KWSpIjEJovjLpUkRSQ2WRx3\nqY4bEYlV1sZdKkmKSOxKibF0LrKdE6WSpIjELkvDgHROUkRilbVhQEqSIhKrrA0DUpIUkVhlbRiQ\nkqSIxCprw4DUcSMiscvSMCAlSRFJRFaWX1NzW0QkQmJJ0syWmNl9ZrbdzLaZ2YeD7ceY2d1m9njw\nfU5SMYiINCrJSnIM+Bt3Xw6cDlxmZsuBK4F73P0E4J7gZxGRVEosSbr7Lnd/OLi9H3gMWAScB9wc\n7HYz8I6kYhARaVRTzkma2VLgFGAjsMDddwV3PQssaEYMIiKTkXiSNLMZwHrgCnffF77P3R3wKo+7\nxMwGzGxgz549SYcpIlJRoknSzLopJshb3f37webdZrYwuH8h8Fylx7r7Onfvd/f++fPnJxmmiEhV\nSfZuG3Aj8Ji7fz501wbg4uD2xcAdScUgItKoJAeTrwTeDzxqZpuDbR8DPgvcZmYfBH4PXJBgDCIi\nDUksSbr7g4BVuftNSR1XRCROmnEjIhJBSVJEJIKSpIhIBCVJEZEISpIiIhGUJEVEIihJiohEUJIU\nEYmgJCkiEkFJUkQkgpKkiEgEJUkRSZWh4REeefqPDA2PtDoUQJeUFZEUuWPzIGvXb6G7q4vRQoHr\nzl/B6r5FLY1JlaSIpMLQ8Ahr12/h4GiB/SNjHBwtsGb9lpZXlEqSFaSt3BfpBDtfOEB31/iU1N3V\nxc4XDrQooiI1t8uksdwX6QSL50xjtFAYt220UGDxnGktiqhIlWRIWst9kU4wd0Yv152/gqndXczs\nncLU7i6uO38Fc2f0tjQuVZIhpXL/IC9/mpXK/Va/UCKdYHXfIlYum8fOFw6weM60VPzdKUmGpLXc\nF+kkc2f0piI5lqi5HZLWcl8kaeqsrE6VZJk0lvsiSVJnZTQlyQrSVu6LJCXcWVk6F79m/RZWLpun\nv4GAmtsiHSytYxPTRElSpIOps7I2JUmRDqbOytp0TlKkw6mzMpqSpIioszKCmtsiIhGUJEVEIihJ\niohEUJIUEYmgJCkiEkFJUkQkgpKkdBStdiMTpXGS0jG02o1MhipJ6Qi6NIdMlpKkdAStdiOTlViS\nNLObzOw5M9sa2na1mQ2a2ebg65ykji8SptVuZLKSrCS/CZxdYfsX3L0v+LorweOLHKbVbmSyEuu4\ncfcHzGxpUs8vMlFa7UYmoxXnJC83sy1Bc3xOC44vba6RYTxzZ/Ry8pLZSpBSt2Ynya8CfwL0AbuA\n66vtaGaXmNmAmQ3s2bOnWfFJyt2xeZCV197L+76xkZXX3suGzYOtDkkyrqlJ0t13u3ve3QvA14FT\nI/Zd5+797t4/f/785gUpqaVhPNIKTU2SZrYw9OM7ga3V9hUpp2E80gqJddyY2beBVcA8M9sJfBJY\nZWZ9gANPAn+d1PElezSMR1ohyd7tCytsvjGp40n2lYbxrCmbWqhOGEmS5m5LW9EwHmk2JUlpO7po\nlTST5m6LiERQkhQRiaAkmXJaJFaktXROMsW0SGzxQ0KdNNJKSpIpFZ5dcpDi2MA167ewctm8jkkW\n+pCQNFBzO6U6fXaJpiBKWihJplSnzy7p9A8JSQ8lyZTq9EViO/1DQtJD5yRTrJNnl2gKoqSFkmTK\ndfLskk7+kJD0UJKUVOvkDwlJB52TFBGJoCQpIhJBSVJEJIKSpIhIBCVJEZEISpIZohWDROKnIUBt\noJ6VcLQYRPy0ApGAkmRqlf5Atw7u5ZofbY9MfloxKH760JESJcmYxFl1lP5Ac2a8eCgPEJn8SotB\nlPaBlxeDUJKcOH3oSFhdSdLMVrr7Q7W2dao4q47wH2gllZKfFoOIlz50JKzejpsv1bmt48S97mGl\nJcLCKiW/Tl8xKG760JGwyErSzM4AXgfMN7OPhO46GsglGVi7iLvqqPQHCjC9N0e+4FWTnxaDiI9W\nIJKwWs3tHmBGsN/M0PZ9wLuSCqqdxF11VPoDverc5Zy0aFbN5KfFIOKjDx0pMXevvZPZK939902I\np6L+/n4fGBho1eFr2rB58Iiqo9GeUA0/EUmemW1y9/6ofWo1t/+3u18BfNnMjsim7r66wRgzIYmq\nQ1WhSDrUam7fEnz/x6QDaXdKaiLZVCtJfg54E3COu69tQjwiIqlSK0kuNLPXAavN7DuAhe9094cT\ni0xEJAVqJclPAFcBi4HPl93nwBuTCEpEJC0ik6S73w7cbmZXufs1TYpJRCQ16pqW6O7XmNlq4Kxg\n0/3ufmdyYYmIpENd0xLN7DPAh4HtwdeHzewfkgxMRCQN6l0F6Fygz90LAGZ2M/Ar4GNJBSYikgYT\nWZl8duj2rLgDERFJo3qT5GeAX5nZN4MqchPw91EPMLObzOw5M9sa2naMmd1tZo8H3+dMPnTpBLok\nhbRazSRpZgY8CJwOfB9YD5zh7t+t8dBvAmeXbbsSuMfdTwDuCX4WqeiOzYOsvPZe3veNjay89l42\nbB5sdUjSgWomSS+ugHGXu+9y9w3B17N1PO4B4A9lm88Dbg5u3wy8Y6IBS2eIe51Okcmqt7n9sJn9\n1xiOt8DddwW3nwUWxPCckkGVFh8urdMp0kz19m6fBrzPzJ4EXqQ4PdHdfcVkD+zuXmlloRIzuwS4\nBOD444+f7GGkTWl1cEmLepPkW2I63m4zW+juu8xsIfBctR3dfR2wDorrScZ0fGkTWh1c0qLWepJT\ngUuBZcCjwI3uPtbA8TYAFwOfDb7f0cBzScZpdXBJg1qV5M3AKPAz4K3Acoozb2oys28Dq4B5ZrYT\n+CTF5HibmX0Q+D1wweTClk6hdTql1WolyeXu/mcAZnYj8Mt6n9jdL6xy15vqfQ4RkVar1bs9WrrR\nYDM7NTQ4OVv0ekrSalWSJ5vZvuC2AdOCn0u920cnGl3M7tg8yNqYL9glraPXU5ohspJ095y7Hx18\nzXT3KaHbbZUgNTg5W/R6SrNMZIGLtqbBydmi11OapWOSpAYnZ4teT2mWjkmSpcHJU7u7mNk7hand\nXRqc3Mb0ekqzWHH9inTr7+/3gYGBWJ5raHhEg5MzRK+nNMLMNrl7f9Q+9U5LzAwNTs4WvZ6StI5p\nbouITIaSpIhIBCVJSYxmw0gWdNw5SWkOzYaRrFAlKUC8VZ9mw0iWqJKU2Ku+0myYg7w82Ls0G0Y9\n0dJuVEl2kErVYhJVn2bDSJYoSXaIapdnTWIOtGbDSJaoud0BwtViqQm8Zv0WVi6bl1jVp0svSFao\nkiS9Q1XiiiuqWkyy6ps7o5eTl8xWgpS21vGVZFqHqsQZV61qUVWfSHUdXUmmdahK3HHVUy3WW/Wl\nteoWSUpHV5JpHaqSRFxxVItprbpFktTRlWRah6pMJq56KrxGzhGmteoWSVpHJ8m5M3q5oH/xuG0X\n9C9OpIosT2JRSW2inSnVhvdMJK4du/dHJlldLkE6VUc3t4eGR7htYOe4bbcN7OTDb3r1EQmpkcVd\ny5upF/Qv5raBnRWbraXjrFw2j4fWvrHmMaOG99SKsxSXF5yRvDO1u5gEKzWj01p1iySto5Nkvef+\nGjkXVymJ3fLzpwCOSGoP7nh+wseZ7PnLcFwlpduVkmypul1TFp96wiXrOjpJ1lMdNVKpQeUkVq67\nq4ttz+yd1HEmW+FFxVUtyWqokHSijj8nWevcX6Pn4iolsXLF+21Sx5nsYPCouKKSrAaIS6fp6EoS\naldHjZ6Lq9RMrXRO8sTjjp70cSZT4YXjqnROUklQpKjjrpY4GRs2Dx5OcofyeS5/wwm897TjJ5RI\nyjt+KnUEhY/TrHGIpTim9+R48VBezWjpKPVcLVFJsk5DwyPcuvEpbrhvBz255JKYLpEq0jy6pGzM\nvnL/DkbGCoyMTbwDp166RKpIumSy4yaJ+cXNHEyt+dEi6ZG5SjKp+cXNGkyt+dEi6ZKpSjKJ+cWl\nqg5IfLVtzY8WSZ9MVZJxr55TqaqLmirYaKdLnPGnoQMoDTGINCpTSTLOJnGlmTZ/e/sjfP2ifk48\nbtYRf/RxNJPjij8NTfY0xCASh0w1t0sDpHundHFUT47eKZNvElfqkBkZcy791sNHrLQTVzO53tkz\nUR07aWiypyEGkbi0pJI0syeB/UAeGKs1TmkivPSv2+GfJmN6T27c4g8lLx3KA+OH/8TZTK41e6ZW\nhZaGhYTTEINIXFpZSb7B3fviTJClCmZkzHlpNM/ImE+6gnlm78HI+8PDf+ptJtc7tKfa/Oh6KrQ0\nLGmWhhhE4pKp5na8Yxmjq9DwH315M7l3inHZqmXj9m9kYdySev5/abjmdRpiEIlLqzpuHPiJmTnw\nT+6+Lo4njbOCOfG4WXTnjNH8+GQ5vTdHvuBH/NGXmsmlqYvrHniCG+7fwXXnr2DlsnkNLbc20f9f\nGpY0S0MMInFoVSV5pru/BngrcJmZnVW+g5ldYmYDZjawZ8+eup50IhVMrabv3Bm9XP/uk8d1Av39\nO07iX/776Ty09o1Ve2pLUxfDzeFtz+yLpcKdyP8vDUuapSEGkUa1pJJ098Hg+3Nm9gPgVOCBsn3W\nAeuguMBFvc9dTwVT7/CUiVZD1ToswKtWgBMdS6gKTaS5mp4kzWw60OXu+4PbbwY+HecxohaJmOhK\n4xNZcKJac/jE42ZVvPTBZC7XMNGYRKQxragkFwA/MLPS8f/F3f9vsw6+7Zm9dBWPfVhcw1MqLbB7\n1duWs+2Zvcw+qodvfeBUnhx6ib4ls5kzvYeV197b8HlKEUlW05Okuz8BnNzs40Kxmb3m9kcYGRvf\neo9zeEq4Obx1cC9Xb9g2rvOntPr3ZauW1TWWUFP7RForU9MSo4THUIY1MiunmtJzXfBPPz+id7w0\nQP3L9+2gfJjRyFie6T25wz9rap9I62VqnGSUSmMMj+rO8fWL+hNJPDtfOECXVb+/J9fF5W84gand\nXfTmijt2dRlv+/KDbNg8OOmpfVqLUiReHZMkK3WqFHBOPO7ohp63WlLaOriXAxWmNZaMFgq897Tj\nufPyM/HgHOnB0UJo2NDeCQ8bimPAuoiMl8kkWSlxJTELpFpSGhoe4Zofba/6uO6cHT72i4fy9OaO\nTIZgExoYr0UlRJKRuXOSUefxJjvGsFLnSdRQokrjJcO6DFYumwdEDRs6uuKwoWoxa1EJkWRkKklG\nJS7gcKI7ecnsup+zWtKNSkqVEl9YTy53OHlVGjZUSoYTSepaVEIkGZlKktUS160bn+Ir9+94eezi\nucs5adGsmoknKulGJaVw4suZ8WKwvFr5fiVRybDegeNRyVZEJi9TSbJS4jqUz3PDfcX51KVE9/Ef\nbmVGb46xYKGKar3bUdXiyUtmV01KQ8MjvHLudO68/ExePJRn6zN7uebO7ZHJK45ZNJqyKBK/TCXJ\nStXUZauWse6BJw5fK7tkeKRY3X309i0sX3g0yxbMPOL5ajVhKyWlSs3zvzjtlZx94iuakrw0ZVEk\nXuY++dW7m6W/v98HBgbq3j/c0QIcnv5XTXcOrn9337iKsvQcWwf3cs2Pttc1oHtoeOSIY03t7uKh\ntW9U4hJJITPbVGvh70xVkiXl1VTU+UGA0Tx85LbNh+dNl1eDV71tOScdV/scpnqYRbInk+Mky63u\nW8RDa9/IV9/3WnJVZsGMFWDbM/sqjje85s7tdTWT1cMskj2ZTJLVBpPPmtbNUT1RxbM3dAkIXbZA\nJHsy19yOGkweNX6xO2eceNwsgIaqQfUwi2RLpirJWlPzwpVeacmy7pzRO6WL69998rjB3Y1Ug7ps\ngUh2ZKqSrKfjJFzpTe/JBZeO9cNVZHifbc/sO+I+EeksmUqS9XaclCrGqKb5ZC+tICLZkqnm9kSv\nllitaa4VdUSkJFOVJNTfcRLVNC/d1nhHEclckoSXL58QHrZTnjRrNc013lFEIKNJMnyu8cDoGGbG\n1Cm5cecWa62aoxV1RAQyOHe70vzpsPBc6qHhEX7+uyGeHx7hpOOOpntK7oiFdTXeUSS7OnLudq1V\nwUv7PLjjeT76vUfGXc2wN2dYl42rNpUcRTpbpnq3IXpWDRQvtjU6lmfN7VuOuNzrSN7Vky0i42Qu\nSYaHAR0VuoZ1SW/OeHLoJXIR13utd662iGRf5prbEJ4xs5cP3TLAyNjLFaN1GX1LZpMvVD8XG+7J\n1nlJkc6WuUqyZO6MXs569bF87l0nHzG4fNmCmXzuXSvoLls3racLenLGVecuPzwjR9exFulsmevd\nrqRaNTg0PMK2Z/YCxmO79nH93b+lJ2eMFZyr3raca+7crlXGRTKsI3u3Kwn3Uu/YvZ/NT/+RviWz\nWbZgJme9+liGhke45J8HODRW4NBY8TGf+tftdJedt6w160ZNc5Hs6YgkWfKJHz7KLb946vDPF51x\nPJ8+788qT1HMGaNj9c+6iVosQ0TaV2bPSZbbsXv/uAQJcMvPn2LH7v0snjONA6Nj4+4bGc3zybef\n2PBiGSLS3jqmktz89B8rbn9wxx7efvIizAwI9YKbcfZJr+C0Vx0zrnleiS4AJpJdHZMk+5bMrrj9\nH+56jP0H88W53fmXq8mpU3LcuvEpvnL/jppNaF0ATCS7MtvcLr8Y2Mb/9wcqjR8/lIcv3ftbDuUL\nZdsL3HDf43U1oXUBMJHsymQlWd6JsnrFQm7bVH2M46E8nHvSsdzzm+cOP+ayVctY98ATjIy9XF1G\nNaF1ATCRbMpckgx3opTOEUYlyJKf/vo5fvQ/z+TFQ/nDzeQb7t8xbp9D+QJ7D4wyNDxSMQlqQQyR\n7Mlcc7vSdbPr0ZPr4sVD+cNXOSxvQnfnjHyhwGW3Ppz47JtK1w0XkdZoSSVpZmcDXwRywDfc/bNx\nPXetVYCqqdTRcsQc8DzsHyk2v9es38LKZfNirxw13lIkXZpeSZpZDrgBeCuwHLjQzJbH9fxzZ/Ry\n1bn1P930nlxkR8vcGb3MmtZDT278ikJJrBSk8ZYi6dOKSvJUYIe7PwFgZt8BzgO2x3WAkxbNYkZv\njuGR/OFtU7u7wOFgaBbN9N4cn3r7ibzhPx8bWRE2a4iPxluKpE8rzkkuAp4O/bwz2BabxXOmMVa2\nFJq7U76UR77gNRMkNG+Ij8ZbiqRPanu3zewS4BKA448/fkKPrXaRL2DSF/dqxhCfWhcnE5Hma/pS\naWZ2BnC1u78l+PnvANz9M9UeM9ml0iqtytMOK/W0Q4wiWZDWpdL+AzjBzF4FDALvAd6bxIEqjVts\nh7GM7RCjSKdoepJ09zEzuxz4McUhQDe5+7ZmxyEiUo+WnJN097uAu5I+jpqtItKo1HbcNEqDskUk\nDpmblggalC0i8clkkqw0f1vX0haRychkkqw0KPtQXoOyRWTiMpkkS4Oyw9fVzhcKPLTj+RZGJSLt\nKJNJEmDlsnnjViIfKzCp85Jatkyks2W2d3vnCwfoyeXqXlm8EvWQi0hmK8lGF4tQD7mIQIaTZKMr\n96iHXEQgw81taGzlHi1bJiKQ4UqyZO6M3sPXrZno43SZWBHJdCXZKF0mVkSUJGvQsmUinS3zzW0R\nkUYoSYqIRFCSFBGJkMkkqamEIhKXzHXcaCqhiMQpU5WkphKKSNwylSQ1lVBE4papJKmphCISt0wl\nSU0lFJG4Za7jRlMJRSROmUuSoKmEIhKfTDW3RUTipiQpIhJBSVJEJIKSpIhIBCVJEZEISpIiIhGU\nJEVEIihJiohEMHdvdQw1mdke4PcTeMg84PmEwpksxVQfxVQfxVSfWjG90t3nRz1BWyTJiTKzAXfv\nb3UcYYqpPoqpPoqpPnHEpOa2iEgEJUkRkQhZTZLrWh1ABYqpPoqpPoqpPg3HlMlzkiIicclqJSki\nEou2TpJm9qSZPWpmm81soML9Zmb/x8x2mNkWM3tNwvH8aRBL6WufmV1Rts8qM9sb2ucTCcRxk5k9\nZ2ZbQ9uOMbO7zezx4PucKo+9ONjncTO7OOGYPmdmvw5emx+Y2ewqj418nWOO6WozGwy9PudUeezZ\nZvab4L11ZcIxfTcUz5NmtrnKY2P/PZnZEjO7z8y2m9k2M/twsL1l76eImJJ5P7l7234BTwLzIu4/\nB/g3wIDTgY1NjC0HPEtxHFZ4+yrgzoSPfRbwGmBraNt1wJXB7SuBays87hjgieD7nOD2nARjejMw\nJbh9baWY6nmdY47pauCjdby2vwP+E9ADPAIsTyqmsvuvBz7RrN8TsBB4TXB7JvBbYHkr308RMSXy\nfmrrSrIO5wG3eNEvgNlmtrBJx34T8Dt3n8gg+Fi4+wPAH8o2nwfcHNy+GXhHhYe+Bbjb3f/g7i8A\ndwNnJxWTu//E3ceCH38BLI7jWI3EVKdTgR3u/oS7HwK+Q/H3m2hMZmbABcC34zhWnfHscveHg9v7\ngceARbTw/VQtpqTeT+2eJB34iZltMrNLKty/CHg69PPOYFszvIfqb+YzzOwRM/s3MzuxSfEscPdd\nwe1ngQUV9mnl7+sDFKv+Smq9znG7PGiy3VSlGdmq39Prgd3u/niV+xP9PZnZUuAUYCMpeT+VxRQW\n2/up3a9xc6a7D5rZscDdZvbr4JO4pcysB1gN/F2Fux+m2AQfDs53/RA4oZnxububWWqGNZjZx4Ex\n4NYquzTzdf4qcA3FP6RrKDZvP5DQsSbqQqKryMR+T2Y2A1gPXOHu+4pFbVGr3k/lMYW2x/p+autK\n0t0Hg+/PAT+g2AwKGwSWhH5eHGxL2luBh919d/kd7r7P3YeD23cB3WY2rwkx7S6dagi+P1dhn6b/\nvszsL4G3AX/hwQmjcnW8zrFx993unnf3AvD1Ksdqxe9pCvDfgO9W2yep35OZdVNMRre6+/eDzS19\nP1WJKZH3U9smSTObbmYzS7cpnrTdWrbbBuAiKzod2BtqIiSp6ie+mb0iOLeEmZ1K8TUYakJMG4BS\n7+LFwB0V9vkx8GYzmxM0M98cbEuEmZ0NrAFWu/tLVfap53WOM6bwOet3VjnWfwAnmNmrglbDeyj+\nfpP058Cv3X1npTuT+j0F79Ubgcfc/fOhu1r2fqoWU2Lvpzh6wFrxRbFn8ZHgaxvw8WD7pcClwW0D\nbqDYE/ko0N+EuKZTTHqzQtvCMV0exPsIxZPLr0sghm8Du4BRiueBPgjMBe4BHgd+ChwT7NsPfCP0\n2A8AO4Kvv0o4ph0Uz1ltDr6+Fux7HHBX1OucYEz/HLxXtlBMBAvLYwp+Podir+rvko4p2P7N0nso\ntG/ivyfgTIqnHraEXqdzWvl+iogpkfeTZtyIiERo2+a2iEgzKEmKiERQkhQRiaAkKSISQUlSRCSC\nkqQ0jZnlg5VXtprZ98zsqJif/y/N7Ms19lllZq8L/XypmV0UZxySLUqS0kwH3L3P3U8CDlEcP9ps\nq4DDSdLdv+but7QgDmkTSpLSKj8DlgGY2UeC6nKrBetvmtnSYG3AW83sMTO7vVR5BusBzgtu95vZ\n/eVPbmZvN7ONZvYrM/upmS0IFkO4FPhfQUX7eiuuH/nR4DF9ZvaL0HqEc4Lt95vZtWb2SzP7rZm9\nPvlfj6SFkqQ0XTAP+a3Ao2b2WuCvgNMorvn5ITM7Jdj1T4GvuPt/AfYB/2MCh3kQON3dT6G4lNka\nd38S+BrwhaCi/VnZY24B1rr7Coqzbj4Zum+Ku58KXFG2XTJOSVKaaZoVV9UeAJ6iOP/2TOAH7v6i\nFxf++D7FJcEAnnb3h4Lb3wr2rddi4Mdm9ijwt0DkknRmNguY7e7/Hmy6meICuCWlRRQ2AUsnEIe0\nuXZfKk3aywF37wtvCC+5VUH5nNnSz2O8/AE/tcpjvwR83t03mNkqiiuON2Ik+J5HfzcdRZWktNrP\ngHeY2VHBqizvDLYBHG9mZwS330uxCQ3F5fdfG9w+v8rzzuLlZbnC11bZT3HJ/3HcfS/wQuh84/uB\nfy/fTzqPkqS0lBeX4f8m8LV20/EAAACBSURBVEuKq0t/w91/Fdz9G+AyM3uM4jVSvhps/xTwRSte\nxClf5amvBr5nZpuA50Pb/xV4Z6njpuwxFwOfM7MtQB/w6Ub+b5INWgVIUinoib4zGC4k0jKqJEVE\nIqiSFBGJoEpSRCSCkqSISAQlSRGRCEqSIiIRlCRFRCIoSYqIRPj/wznT6vIONOwAAAAASUVORK5C\nYII=\n",
            "text/plain": [
              "<Figure size 360x360 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QrnXygZR1NuA",
        "colab_type": "code",
        "outputId": "b3d8d855-d1d1-40d9-c006-310b22ed80eb",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "\n",
        "\n",
        "\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "fatal: not a git repository (or any of the parent directories): .git\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}