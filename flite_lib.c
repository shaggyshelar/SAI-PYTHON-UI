#include <Python.h>
#include "include/flite.h"

cst_voice *register_cmu_us_kal(const char *voxdir);

static PyObject *textToWave(PyObject *self, PyObject *args)
{
    char *text_to_convert;
    if (!PyArg_ParseTuple(args, "s", &text_to_convert))
    {
        return NULL;
    }
    cst_voice *v = register_cmu_us_kal(NULL);
    // flite_text_to_speech(text_to_convert, v, "sagar-sai-check.wav");
    cst_wave *waveData = flite_text_to_wave(text_to_convert, v);
    
    float dur = (float)waveData->num_samples / (float)waveData->sample_rate;
    // int sampleRate = waveData->sample_rate;
    int numberOfSamples = waveData->num_samples;
    // int numberOfChannels = waveData->num_channels;
    short *samples = waveData->samples;

    printf("\n File writing done %d, dur = %f, char= %hd \n", numberOfSamples, dur, samples[49]);
    
    PyObject *python_val = PyList_New(numberOfSamples * 2);
    int currentIndex = 0;
    for (int i = 0; i < numberOfSamples; ++i)
    {
        short value = samples[i];
        char a;
        char b;
        a = value;
        value = value >> 8;
        b = value;
        PyObject *python_int1 = Py_BuildValue("c", a);
        PyObject *python_int2 = Py_BuildValue("c", b);
        PyList_SetItem(python_val, currentIndex++, python_int1);
        PyList_SetItem(python_val, currentIndex++, python_int2);
    }
    return python_val;
    // return Py_BuildValue("iiif[cc]", sampleRate,numberOfSamples,numberOfChannels, dur,samples[49],samples[50]);
}

static PyMethodDef myMethods[] = {
    {"textToWave", textToWave, METH_VARARGS, "Convert text to wave"},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef fliteLib = {
    PyModuleDef_HEAD_INIT,
    "fliteLib",
    "Flite library to be used in python",
    -1,
    myMethods};

PyMODINIT_FUNC PyInit_fliteLib(void)
{
    return PyModule_Create(&fliteLib);
}