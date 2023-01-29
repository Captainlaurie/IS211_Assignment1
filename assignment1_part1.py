{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "d63ff673",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def list_divide(numbers, divide = 2):\n",
    "    \"\"\"\n",
    "    The function returns the number of elements in the numbers list that are divisible by divide\n",
    "    \"\"\"\n",
    "    numcount = 0\n",
    "    for x in numbers:\n",
    "        if x % divide == 0:\n",
    "            numcount += 1\n",
    "    return numcount\n",
    "\n",
    "#class that raises exception\n",
    "class ListDivideException(Exception):\n",
    "    pass\n",
    "\n",
    "\n",
    "def test_list_divide():\n",
    "    \"\"\"\n",
    "    Test list_divide\n",
    "    \"\"\"\n",
    "    \n",
    "    try:\n",
    "        \n",
    "        assert list_divide([1,2,3,4,5]) == 2\n",
    "        assert list_divide([2,4,6,8,10]) == 5\n",
    "        assert list_divide([30, 54, 63,98, 100], divide = 10) == 2\n",
    "        assert list_divide([]) == 0\n",
    "        assert list_divide([1,2,3,4,5], 1) == 5\n",
    "        \n",
    "    except AssertionError:\n",
    "        raise ListDivideException\n",
    "        \n",
    "if __name__ == \"__main__\":\n",
    "    \n",
    "    test_list_divide()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8b0008a8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
