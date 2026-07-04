---
type: note
date: "2026-05-19"
tags: [note, technical, digital-cinema, dcp, media-formats, video-engineering, file-formats]
status: inbox
created: "2026-05-19T00:00:00"
---

# DCPRip — Extracting Content from Digital Cinema Packages

## What Is a DCP?

A **Digital Cinema Package (DCP)** is the standard format used to distribute feature films, trailers, and advertisements to movie theaters. Defined by the **Digital Cinema Initiatives (DCI)** consortium — formed by the major Hollywood studios — the format is governed by the SMPTE 428 and related standards.

Key characteristics:

- **Container**: MXF (Material eXchange Format) files wrapped in an XML-based package
- **Video codec**: JPEG 2000 (J2K), not H.264 or HEVC — chosen for its lossless/near-lossless quality and frame-level random access
- **Audio**: Linear PCM, typically 48 kHz or 96 kHz, 24-bit, up to 16 channels
- **Color space**: XYZ color space (not Rec.709 or Rec.2020) at 12 bits per component — wider than typical display primaries
- **Resolution**: 2K (2048×1080) or 4K (4096×2160) are the two DCI-standard resolutions
- **Frame rates**: 24, 25, 30, 48, 60 fps (HFR variants)
- **Encryption**: Most commercial DCPs are encrypted using **AES-128** with keys (KDMs — Key Delivery Messages) time-locked to a specific theater and playback window

### DCP Package Structure

```
MyFilm_FTR_S_EN-XX_51_2K_20240101_IOP/
├── ASSETMAP.xml          — inventory of all files in the package
├── VOLINDEX.xml          — disk layout (for multi-disc packages)
├── CPL_<uuid>.xml        — Composition Playlist: defines reel order, sync, encryption flag
├── PKL_<uuid>.xml        — Packing List: file hashes for integrity checking
└── <uuid>_j2c.mxf        — video essence (JPEG 2000 frames in MXF wrapper)
└── <uuid>_pcm.mxf        — audio essence (PCM in MXF wrapper)
```

There are two DCP flavors:
- **Interop (IOP)**: older, pre-SMPTE, widely deployed; more compatible
- **SMPTE**: newer standard with stricter spec compliance; increasingly required

---

## What Is DCPRip?

"DCPRip" refers to the process — and associated tooling — of **extracting the raw audio and video essence from a DCP** and converting it to a more universally playable format (e.g., ProRes, H.264, WAV).

This is done for legitimate purposes such as:

- **Post-production QC**: studios and distributors verify the DCP matches the deliverable spec before theatrical release
- **Archival**: creating access copies for preservation alongside the theatrical master
- **Restoration and re-release**: extracting legacy DCP content for a remaster workflow
- **Localization**: pulling picture to add new subtitle tracks or audio mixes
- **Educational and research use**: film schools, cinematographers, colorists studying theatrical color pipelines

**Encrypted commercial DCPs cannot be ripped without a valid KDM** — the decryption key is bound to specific equipment certificates. Ripping an encrypted DCP without authorization is a violation of copyright law (DMCA in the US, similar statutes elsewhere).

---

## Tools

### Open-Source

| Tool | Role |
|------|------|
| **`asdcplib`** | SMPTE-standards library for reading/writing MXF essence; foundational dependency for most DCP tools |
| **`opendcp`** | Open-source DCP creation and inspection tool; can decode unencrypted J2K MXF to image sequences |
| **`DCP-o-matic`** | Full DCP creation suite; can also inspect and partially decode DCP content; widely used in indie film |
| **`dcptools`** / `libdcp` | Carl Hetherington's library and CLI; used in Dolby and indie workflows; strong SMPTE compliance |
| **`ffmpeg`** (with limitations) | Can decode JPEG 2000 MXF files to various output formats — most practical for unencrypted DCPs |
| **`grok`** / `OpenJPEG` | Open-source JPEG 2000 decoders; used under the hood by ffmpeg and opendcp |

### Commercial

| Tool | Role |
|------|------|
| **Clipster** (Rohde & Schwarz) | High-end DCP mastering and QC workstation |
| **easyDCP** | Common commercial DCP creation/QC tool; supports KDM-based decryption |
| **Fraunhofer EasyDCP** | Used by studios; supports full decrypt + transcode workflow |
| **Colorfront** | Used in post houses for HDR/DCI mastering and DCP verification |

---

## Technical Process (Unencrypted DCP)

### Step 1: Parse the package structure

Read `ASSETMAP.xml` → identify CPL → identify MXF track files.

### Step 2: Demux MXF essence

Extract JPEG 2000 frames from the video MXF. Each frame is a standalone J2K codestream. Audio MXF contains interleaved PCM samples.

```bash
# Using ffmpeg to extract video as a TIFF image sequence from a J2K MXF
ffmpeg -i video_<uuid>.mxf -vf "colorspace=iall=bt709:all=bt709" frame_%06d.tiff

# Extract audio PCM to WAV
ffmpeg -i audio_<uuid>.mxf output.wav
```

### Step 3: Color space conversion

DCP uses the **CIE XYZ color space** with a specific non-linear transfer function. To get Rec.709 (standard HD) output:

- Convert from XYZ → Rec.709 primaries using a 3x3 matrix transform
- Apply gamma correction (DCI gamma is approximately 2.6; Rec.709 uses ~2.4)
- This is critical — without it, colors will be heavily shifted and the image will appear washed out

`ffmpeg`'s `colorspace` filter handles this, but professional workflows use dedicated color management (ACES, LUT-based, or color-managed transcoder).

### Step 4: Assemble output

Combine image sequence + audio into a delivery format:
- **ProRes 4444** or **ProRes HQ**: common for editorial/archival
- **H.264/H.265**: for access copies or review
- **DPX**: for VFX or restoration workflows (preserves full bit depth)

---

## Key Technical Constraints

| Constraint | Detail |
|------------|--------|
| Encryption | AES-128 KDM required; without it, MXF files are unreadable |
| Color space | XYZ → Rec.709/P3 conversion required for accurate output |
| Codec | JPEG 2000 decode is computationally expensive vs. H.264 |
| Frame rate | Some HFR DCPs (48fps) can trip up naive tools expecting 24fps |
| Audio channels | Up to 16 channels; most tools default to stereo downmix |
| Subtitles | Stored as separate XML/MXF asset; requires separate extraction |
| Reels | Long films are split into multiple reels; all must be concatenated |

---

## Legal and Ethical Context

DCPRip workflows are standard in professional post-production. Studios, distributors, and post houses routinely perform these operations as part of QC, localization, and archival pipelines.

The legal risk arises exclusively with:
1. Decrypting a KDM-protected DCP without authorization
2. Reproducing or distributing the extracted content without rights

For security professionals: KDM systems are a notable example of **time-locked cryptographic access control** in a high-stakes commercial environment — an applied cryptography case study worth understanding regardless of the media context.

---

## Connections

- [[02-Areas/Learning/Self-Study/Technical/2026-05-17 — M-DISC — Archival Optical Storage|M-DISC — Archival Optical Storage]] — complementary archival media format; both concern long-form digital preservation; M-DISC targets storage longevity, DCP targets secure distribution — two different axes of the same archival problem
- [[MOC/Technical|Technical MOC]] — parent map of content
- [[MOC/Work — Security|Work — Security]] — AES-128 KDM encryption is applied cryptography; the KDM time-lock pattern (binding a decryption key to specific hardware + time window) is a concrete example of cryptographic access control in a commercial high-stakes environment
- [[02-Areas/Work/Security/2026-03-22 — NIST SP 800-171r2 CUI Security Requirements|NIST SP 800-171r2 CUI Security Requirements]] — 3.13.10 (cryptographic key management) and 3.13.11 (FIPS-validated cryptography) are the compliance-side articulation of the same principles KDM systems implement operationally; the DCI KDM architecture is effectively a real-world deployment of key lifecycle management at scale
- JPEG 2000 and color science → potential connection to future Physics/optics or signal processing notes
