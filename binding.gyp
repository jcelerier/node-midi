{
  'targets': [
    {
      'target_name': 'midi',
      'include_dirs': [
        "<!(node -e \"require('nan')\")",
        'src',
        'src/lib/RtMidi17',
        'src/lib/weakjack'
      ],
      'sources': [
        'src/node-midi.cpp'
      ],
      'conditions': [
        ['OS=="linux"',
          {
            'cflags_cc!': [
              '-fno-exceptions'
            ],
            'cflags_cc': [ '-std=c++1z' ],
            'defines': [
              'RTMIDI17_ALSA',
              'RTMIDI17_JACK',
              'RTMIDI17_HEADER_ONLY'
            ],
            'link_settings': {
              'libraries': [
                '-lasound',
                '-pthread',
              ]
            }
          }
        ],
        ['OS=="mac"',
          {
            'cflags_cc': [ '-std=c++1z' ],
            'defines': [
              '__MACOSX_CORE__',
              'RTMIDI17_JACK',
              'RTMIDI17_HEADER_ONLY'
            ],
            'xcode_settings': {
              'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
            },
            'link_settings': {
              'libraries': [
                'CoreMIDI.framework',
                'CoreAudio.framework',
                'CoreFoundation.framework',
              ],
            }
          }
        ],
        ['OS=="win"',
          {
            'configurations': {
              'Release': {
                'msvs_settings': {
                  'VCCLCompilerTool': {
                    'ExceptionHandling': 1
                  }
                }
              }
            },
            'cflags_cc': [ '/std:c++latest' ],
            'defines': [
              'RTMIDI17_WINMM',
              'RTMIDI17_JACK',
              'RTMIDI17_HEADER_ONLY'
            ],
            'link_settings': {
              'libraries': [
                '-lwinmm.lib'
              ],
            }
          }
        ]
      ]
    }
  ]
}
