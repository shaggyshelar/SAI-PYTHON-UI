#include <stdio.h>
#include "include/flite.h"

int i2s_stream_chunk(const cst_wave *w, int start, int size,
                     int last, cst_audio_streaming_info *asi);
void start_conversion();

cst_voice *register_cmu_us_kal(const char *voxdir);

int i2s_stream_chunk(const cst_wave *w, int start, int size,
                     int last, cst_audio_streaming_info *asi)
{
    if (last == 1)
    {
        // Nothing
    }

    printf("start = %d", start);

    /* if you want to stop return CST_AUDIO_STREAM_STOP */
    return CST_AUDIO_STREAM_CONT;
}

void start_conversion()
{
    cst_voice *v = register_cmu_us_kal(NULL);
    cst_audio_streaming_info *asi =
        cst_alloc(struct cst_audio_streaming_info_struct, 1);
    asi->min_buffsize = 256;
    asi->asc = i2s_stream_chunk;
    asi->userdata = NULL;
    feat_set(v->features, "streaming_info", audio_streaming_info_val(asi));
    flite_text_to_speech("Hello World.", v, "test.wav");
}
