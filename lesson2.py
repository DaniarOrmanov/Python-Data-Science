{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "lesson2.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "toc_visible": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7KWduRsl2bO2"
      },
      "source": [
        "# Тема \"Вычисления с помощью Numpy\""
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "D3SPOVHp28Xd"
      },
      "source": [
        "### Задание 1"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eGsLLv6-pH_Z",
        "outputId": "74093cc6-3e27-4c46-bbca-ec96abc43a41"
      },
      "source": [
        "import numpy as np\n",
        "A = np.array([[1, 6],\n",
        "     [2, 8],\n",
        "     [3, 11],\n",
        "     [3, 10],\n",
        "     [1, 7]])\n",
        "A"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[ 1,  6],\n",
              "       [ 2,  8],\n",
              "       [ 3, 11],\n",
              "       [ 3, 10],\n",
              "       [ 1,  7]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jUoGY53LxQFq",
        "outputId": "43dba104-0ff0-4109-ffce-083678a88e14"
      },
      "source": [
        "mean_a = np.mean(A, axis = 0)\n",
        "mean_a"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([2. , 8.4])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fxuyy-g53LEk"
      },
      "source": [
        "### Задание 2"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hps605ya4eT0",
        "outputId": "b9cd5a72-090f-4e85-80af-f89916e7f5e0"
      },
      "source": [
        "a_centered = np.array([A[:, 0] - mean_a[0], A[:, 1] - mean_a[1]]).T \n",
        "a_centered"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[-1. , -2.4],\n",
              "       [ 0. , -0.4],\n",
              "       [ 1. ,  2.6],\n",
              "       [ 1. ,  1.6],\n",
              "       [-1. , -1.4]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 35
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PYNKur72-JfY"
      },
      "source": [
        "##### Получилось кривовато"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "yoVIrcq6-Q1Q"
      },
      "source": [
        "### Задание 3"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "w67Rpkcj-T0-",
        "outputId": "22d7b869-4655-4344-a5e7-697220f24545"
      },
      "source": [
        "a_centered_sp = a_centered[:,0] @ a_centered[:,1]\n",
        "result = a_centered_sp/(a_centered.shape[0] - 1)\n",
        "result"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2.0"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 53
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EZVjQa9TDMgd"
      },
      "source": [
        "### Задание 4"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WS9H-74nDTJE",
        "outputId": "f9ec4090-87eb-4ee9-bb6a-04a44e6079a9"
      },
      "source": [
        "cov = np.cov(A.T)[0, 1]\n",
        "cov"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2.0"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 55
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zPAcT0_yD4wU"
      },
      "source": [
        "# Тема “Работа с данными в Pandas”"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nYwmZQvCEDPU"
      },
      "source": [
        "### Задание 1"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SgmWzU_RECO0",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        },
        "outputId": "c2cebca6-a7be-4f61-95d3-dca27397e372"
      },
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "\n",
        "authors = pd.DataFrame({\n",
        "    \"author_id\": [1,2,3],\n",
        "    \"author_name\": ['Тургенев','Чехов','Островский']})\n",
        "\n",
        "book = pd.DataFrame({\n",
        "    \"author_id\": [1,1,1,2,2,3,3],\n",
        "    \"book_title\": ['Отцы и дети','Рудин','Дворянское гнездо','Толстый и тонкий','Дама с собачкой','Гроза','Таланты и поклонники'],\n",
        "    \"price\": [450,300,350,500,450,370,290]})\n",
        "book.head()"
      ],
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>author_id</th>\n",
              "      <th>book_title</th>\n",
              "      <th>price</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>Отцы и дети</td>\n",
              "      <td>450</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>Рудин</td>\n",
              "      <td>300</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1</td>\n",
              "      <td>Дворянское гнездо</td>\n",
              "      <td>350</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>2</td>\n",
              "      <td>Толстый и тонкий</td>\n",
              "      <td>500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2</td>\n",
              "      <td>Дама с собачкой</td>\n",
              "      <td>450</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   author_id         book_title  price\n",
              "0          1        Отцы и дети    450\n",
              "1          1              Рудин    300\n",
              "2          1  Дворянское гнездо    350\n",
              "3          2   Толстый и тонкий    500\n",
              "4          2    Дама с собачкой    450"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SPgWi7ETnX1s"
      },
      "source": [
        "### Задание 2"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 266
        },
        "id": "35YR7J9MnWPc",
        "outputId": "6ef53000-e811-4d04-c2c5-1e7ce2d1d140"
      },
      "source": [
        "author_price = pd.merge(authors, book, on = 'author_id', how = 'inner')\n",
        "author_price"
      ],
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>author_id</th>\n",
              "      <th>author_name</th>\n",
              "      <th>book_title</th>\n",
              "      <th>price</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>Тургенев</td>\n",
              "      <td>Отцы и дети</td>\n",
              "      <td>450</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>Тургенев</td>\n",
              "      <td>Рудин</td>\n",
              "      <td>300</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1</td>\n",
              "      <td>Тургенев</td>\n",
              "      <td>Дворянское гнездо</td>\n",
              "      <td>350</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>2</td>\n",
              "      <td>Чехов</td>\n",
              "      <td>Толстый и тонкий</td>\n",
              "      <td>500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2</td>\n",
              "      <td>Чехов</td>\n",
              "      <td>Дама с собачкой</td>\n",
              "      <td>450</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>3</td>\n",
              "      <td>Островский</td>\n",
              "      <td>Гроза</td>\n",
              "      <td>370</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>3</td>\n",
              "      <td>Островский</td>\n",
              "      <td>Таланты и поклонники</td>\n",
              "      <td>290</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   author_id author_name            book_title  price\n",
              "0          1    Тургенев           Отцы и дети    450\n",
              "1          1    Тургенев                 Рудин    300\n",
              "2          1    Тургенев     Дворянское гнездо    350\n",
              "3          2       Чехов      Толстый и тонкий    500\n",
              "4          2       Чехов       Дама с собачкой    450\n",
              "5          3  Островский                 Гроза    370\n",
              "6          3  Островский  Таланты и поклонники    290"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KKws4FQBsQT6"
      },
      "source": [
        "### Задание 3"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        },
        "id": "4Y8bxSyhsTQo",
        "outputId": "be753c5c-2068-48e7-8a47-c349f20cbdd9"
      },
      "source": [
        "top5 = author_price.sort_values(by='price', ascending=False).iloc[0:5, :]\n",
        "top5"
      ],
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>author_id</th>\n",
              "      <th>author_name</th>\n",
              "      <th>book_title</th>\n",
              "      <th>price</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>2</td>\n",
              "      <td>Чехов</td>\n",
              "      <td>Толстый и тонкий</td>\n",
              "      <td>500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>Тургенев</td>\n",
              "      <td>Отцы и дети</td>\n",
              "      <td>450</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2</td>\n",
              "      <td>Чехов</td>\n",
              "      <td>Дама с собачкой</td>\n",
              "      <td>450</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>3</td>\n",
              "      <td>Островский</td>\n",
              "      <td>Гроза</td>\n",
              "      <td>370</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1</td>\n",
              "      <td>Тургенев</td>\n",
              "      <td>Дворянское гнездо</td>\n",
              "      <td>350</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   author_id author_name         book_title  price\n",
              "3          2       Чехов   Толстый и тонкий    500\n",
              "0          1    Тургенев        Отцы и дети    450\n",
              "4          2       Чехов    Дама с собачкой    450\n",
              "5          3  Островский              Гроза    370\n",
              "2          1    Тургенев  Дворянское гнездо    350"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 40
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nD7qdRTCvHJW"
      },
      "source": [
        "### Задание 4"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 142
        },
        "id": "QVMvaL4CvKaG",
        "outputId": "e92f1ba9-d603-491b-a11e-6c403b63edb3"
      },
      "source": [
        "author_max = author_price.groupby('author_name').agg({'price':'max'})\n",
        "author_min = author_price.groupby('author_name').agg({'price':'min'})\n",
        "author_mean = author_price.groupby('author_name').agg({'price':'mean'})\n",
        "author_stat = pd.merge(author_max, author_min, on = 'author_name', how = 'inner')\n",
        "author_stat = pd.merge(author_stat, author_mean, on = 'author_name', how = 'inner')\n",
        "author_stat = author_stat.reset_index()\n",
        "author_stat = author_stat.rename(columns={'price_x':'max_price'})\n",
        "author_stat = author_stat.rename(columns={'price_y':'min_price'})\n",
        "author_stat = author_stat.rename(columns={'price':'mean_price'})\n",
        "author_stat"
      ],
      "execution_count": 75,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>author_name</th>\n",
              "      <th>max_price</th>\n",
              "      <th>min_price</th>\n",
              "      <th>mean_price</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Островский</td>\n",
              "      <td>370</td>\n",
              "      <td>290</td>\n",
              "      <td>330.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Тургенев</td>\n",
              "      <td>450</td>\n",
              "      <td>300</td>\n",
              "      <td>366.666667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Чехов</td>\n",
              "      <td>500</td>\n",
              "      <td>450</td>\n",
              "      <td>475.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "  author_name  max_price  min_price  mean_price\n",
              "0  Островский        370        290  330.000000\n",
              "1    Тургенев        450        300  366.666667\n",
              "2       Чехов        500        450  475.000000"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 75
        }
      ]
    }
  ]
}