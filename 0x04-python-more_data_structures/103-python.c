#include <stdio.h>

/**
 * print_python_list - Prints basic info about a Python list
 * @p: Pointer to a PyObject (Python list)
 */
void print_python_list(PyObject *p) {
    Py_ssize_t i, size;
    PyObject *item;

    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

/**
 * print_python_bytes - Prints basic info about a Python bytes object
 * @p: Pointer to a PyObject (Python bytes)
 */
void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");
    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str);

    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++) {
        printf("%02x", (unsigned char)str[i]);
        if (i < 9)
            printf(" ");
    }
    printf("\n");
}
