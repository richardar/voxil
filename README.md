# voxil

**Fast, honest speaker diarization for large piles of long recordings, on your own hardware.**

voxil answers "who spoke when" for batch audio. It runs several open diarization model
families behind one API, adds the systems work the models leave out (long-form handling,
batching, input validation), and publishes reproducible benchmarks for every claim it makes.

> **Status: early development.** Diarization backends are not implemented yet, and the
> APIs below may change. Not ready for production use.

## Why voxil

Good open diarization models exist (pyannote, NVIDIA NeMo, sherpa-onnx), and each is easy
to call on one short file. It gets harder when you have thousands of hours of long,
many-speaker audio:

- End-to-end models have a fixed number of speaker slots, so long recordings with many
  speakers need chunking and cross-chunk speaker linking.
- Pipelines leave the GPU idle during CPU-bound steps, so throughput on large jobs is poor.
- Comparing models fairly on *your* audio, including speed, memory and cost, is mostly DIY.

voxil focuses on those problems. It does not try to replace the model owners' own
libraries.

## The one claim

> The fastest correct way to diarize many long recordings on your own GPU or CPU,
> measured against running the same models directly, with the same weights.

If the benchmarks cannot back that claim, the benchmark itself becomes the deliverable.

## Planned features (first release)

| Area | What to expect |
| --- | --- |
| Backends | pyannote Community-1, Nemotron 3 Diarization / Streaming Sortformer (NeMo), sherpa-onnx (CPU) |
| One result schema | Segments with start, end, speaker and backend metadata; RTTM, JSON and SRT output |
| Python API | `Diarizer(model=..., device="auto")` with `.run(path)` and `.run_batch(paths)` |
| CLI | `voxil diarize`, `voxil batch`, `voxil bench` |
| Input validation | Sample rate, channels, duration, clipping and silence checks before inference |
| Long-form mode | Windowed inference, overlap merging, cross-window speaker linking |
| Batch engine | Directory or manifest input, resumable jobs, results cache, cross-file batching |
| Benchmarks | DER, JER, real-time factor, throughput, peak memory, cost per audio hour |

### Intended usage (not implemented yet)

```python
from voxil import Diarizer

diarizer = Diarizer(model="pyannote", device="auto")
result = diarizer.run("meeting.wav")

for seg in result.segments:
    print(f"{seg.start:7.2f} {seg.end:7.2f} {seg.speaker}")
```

```bash
voxil batch recordings/ --model nemo --out results/ --format rttm
voxil bench recordings/ --refs references/ --models pyannote,nemo,onnx
```

### Later, only if users ask

Streaming with stable speaker labels, a REST/WebSocket server, ONNX/TensorRT export,
speaker identification, calibrated confidence scores, more backends, and transcript
alignment with an ASR model. Training or fine-tuning on your own data is undecided and
will be revisited once the benchmarks show where stock models fall short.

### Out of scope

Bundling or mirroring model weights, closed-weight or API-only backends, and a web UI.

## Roadmap

There are no dates. Work moves through phases, and each ends at a gate:

1. **Foundation**: result schema, CLI, three backend adapters, benchmark harness on AMI,
   VoxConverse and AISHELL-4.
   *Gate A: a defensible stock-model baseline table.*
2. **Engine**: long-form mode and the batch engine.
   *Gate B: a measurable win over naive chunking and a plain loop.*
3. **Release**: docs, Colab, Docker image, results page, design write-up.
   *Gate C: a stranger can reproduce a benchmark row from the docs alone.*
4. **Adoption**: respond to outside users; pull from the "later" list on demand.

## Principles

1. Benchmark first, optimise second.
2. Compare against the same model run directly, and publish losses as well as wins.
3. Systems around the models come first; the first release uses models as published.
4. Keep each backend an isolated, optional install.
5. One result schema everywhere.
6. Respect model owners: download weights from their source and honour gates and licences.
7. Small and finished beats big and half-built.
8. Every published number is reproducible with one command.

## Contributing

Contributions are welcome. Pick an open issue, comment to claim it, and open a pull
request when it's ready. Have an idea outside the current scope? Open an issue labelled
`later`.

## Model licences

voxil's code will be licensed under Apache-2.0. Model weights are **not** part of this
repository and keep their owners' licences. For example, pyannote Community-1 weights are
gated on Hugging Face and require accepting their terms. Check each model's licence
before commercial use.
