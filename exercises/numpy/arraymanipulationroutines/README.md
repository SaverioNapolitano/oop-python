# Array manipulation routines 

Let x be a ndarray with shape (4, 4, 3) with all elements set to zero. Reshape x so that the size of the second dimension equals 12. Use reshape().

---

Let x = np.array([[1, 2, 3], [4, 5, 6]]). Convert it to [1 4 2 5 3 6]. Use ravel().

---

Let x = np.array([[1, 2, 3], [4, 5, 6]]). Get the 5th element.

---

Let x be an arbitrary 3-D array of shape (3, 4, 5). Permute the dimensions of x such that the new shape will be (4,3,5). Use swapaxes().

---

Let x be an arbitrary 2-D array of shape (3, 4). Insert a nex axis such that the new shape will be (3, 1, 4). Use expand_dims().

---

Let x be an arbitrary 3-D array of shape (3, 1, 4). Remove a single-dimensional entries such that the new shape will be (3, 4). Use squeeze().

---

Let x = np.array([[1, 2, 3], [4, 5, 6]]) and y = np.array([[7, 8, 9], [10, 11, 12]]). Concatenate x and y so that a new array looks like np.array([[1, 2, 3, 7, 8, 9], [4, 5, 6, 10, 11, 12]]). Use concatenate().

---

Let x = np.array([[1, 2, 3], [4, 5, 6]]) and y = np.array([[7, 8, 9], [10, 11, 12]]). Concatenate x and y so that a new array looks like np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]). Use concatenate().

---

Let x = np.array([1, 2, 3]). Create a new array like np.array([[1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3]]). Use tile().