#include <Python.h>
#include <float.h>
/**
* print_python_list - prints some basic info about Python lists
* @p: pointer to PyObject struct
*/
void print_python_list(PyObject *p)
{
Py_ssize_t i, n;
PyObject *o;

printf("[*] Python list info\n");
if (!PyList_Check(p))
{
printf("  [ERROR] Invalid List Object\n");
fflush(stdout);
return;
}

n = PyList_Size(p);
printf("[*] Size of the Python List = %ld\n", n);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
for (i = 0; i < n; i++)
{
o = PyList_GET_ITEM(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(o)->tp_name);
}
fflush(stdout);
}

/**
* print_python_bytes - prints some basic info about Python bytes
* @p: pointer to PyObject struct
*/
void print_python_bytes(PyObject *p)
{
Py_ssize_t i, n;
char *s;

printf("[*] Python bytes info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
fflush(stdout);
return;
}
printf("[.] bytes object info\n");
n = PyBytes_Size(p);
printf("  size: %ld\n", n);
s = PyBytes_AsString(p);

printf("  trying string: %s\n", s);
printf("  first %ld bytes:", n + 1 > 10 ? 10 : n + 1);
for (i = 0; i < n + 1 && i < 10; i++)
printf(" %02x", (unsigned char)s[i]);
printf("\n");
fflush(stdout);
}
/**
* print_python_float - prints some basic info about Python float objects
* @p: pointer to PyObject struct
*/
void print_python_float(PyObject *p)
{
char *s;
double value;

printf("[*] Python float info\n");
if (!PyFloat_Check(p))
{
printf("  [ERROR] Invalid Float Object\n");
fflush(stdout);
return;
}
value = PyFloat_AsDouble(p);
s = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
printf("  value: %s\n", s);
fflush(stdout);
}
