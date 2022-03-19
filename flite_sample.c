#include <stdio.h>
#include "include/flite.h"

extern void usenglish_init(cst_voice *v);
extern cst_lexicon *cmulex_init(void);
cst_voice *register_cmu_us_kal(const char *voxdir);

int init() {
  int x = flite_init();
  if (x) {
    printf("Failed to intialize Flite");
    return x;
  }

  flite_add_lang("eng",usenglish_init,cmulex_init);
  printf("**** Flite Initialized ******");
  return x;
}

void* select_voice(const char* path) {
  fprintf("**** Flite Voice Selected = %s ******",path);
  cst_voice *v = flite_voice_load(path);
  return (void*) v;
}

cst_wave* text_to_wave(const char* text) {
  fprintf("**** TextToWave Started for  = %s ******",text);
  cst_voice *v = register_cmu_us_kal(NULL);
  if (!v) {
    printf("Error occurred while converting text to wave.")
    return NULL;
  }    
  return flite_text_to_wave(text, v);
}

// int i2s_stream_chunk(const cst_wave *w, int start, int size,
//                      int last, cst_audio_streaming_info *asi);
// void start_conversion();

// cst_voice *register_cmu_us_kal(const char *voxdir);

// int i2s_stream_chunk(const cst_wave *w, int start, int size,
//                      int last, cst_audio_streaming_info *asi)
// {
//     printf("start = %d", start);
//     /* if you want to stop return CST_AUDIO_STREAM_STOP */
//     return CST_AUDIO_STREAM_CONT;
// }

// void start_conversion()
// {
//     cst_voice *v = register_cmu_us_kal(NULL);
//     cst_audio_streaming_info *asi =
//         cst_alloc(struct cst_audio_streaming_info_struct, 1);
//     asi->min_buffsize = 256;
//     asi->asc = i2s_stream_chunk;
//     asi->userdata = NULL;
//     feat_set(v->features, "streaming_info", audio_streaming_info_val(asi));
//     flite_text_to_speech("Hello World.", v, "test.wav");
// }
