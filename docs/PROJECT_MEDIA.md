# Project images and editorial selection

The project collection contains sixteen independent Chinese/English introductions.
Each explains purpose, architecture, operating stages, results, analysis and scope.
Only source images that remain useful and readable at page size are included.

## Selected images

| Project | Image | Interpretation |
| --- | --- | --- |
| ECsnap | Owner-provided instrument photograph | Prototype enclosure, display and electrode interface; no concentration-performance claim |
| Dual-Axis Gravity Controller | Archived running-vector-mean plot | Model simulation with a 0.380 G reference, not physical gravity reduction |
| Biological Image Analysis | Plant contours and area labels | Saved segmentation output; values depend on original scale and parameters |
| Medical Image Analysis | Two archived digit-classification curves | Training/validation accuracy and loss; historical results |
| Data Structures | Source-0 shortest-path tree | Archived graph result; original graph remains linked at the source repository |
| AFPGA | Lab 8 board photograph | Archived LED and seven-segment state, interpreted with HPS source |
| PressiBLE | Archived open-enclosure photograph | XIAO nRF52840, battery, wiring and mounting; no calibration or battery-life claim |
| PressiBLE | Device-readout screenshot from the ver2 manual | App interaction and displayed states, not an experiment or clinical conclusion |
| SpaceCellCam | Archived on-board imaging integration photograph | Physical mounting with a rotating sample platform; not current AF/standby firmware validation |
| Space Microfluidic Payload | Ground-preparation microvalve manifold photograph | Physical fluid-interface assembly, not flight hardware or qualification |
| ThermoPatch | Archived Android monitoring screen | One populated body-location card and separate BLE connection states; not six simultaneous measurements |
| Galaxy Watch Sensor Monitor | Archived on-demand reading screen | SDK output and stopped tracker state; not core temperature or accuracy validation |
| Smart Stop-Flow | Labeled open-enclosure integration photograph | Pumps, reservoirs, pressure chambers, valves and chip; not calibrated fluid performance |
| Passive PVA Sponge Pump | Microchannel connected to sponge absorber | Physical passive-pump arrangement from a general progress report; not a flow-rate measurement |
| Space BMC Core | Plot of a saved Questa waveform | Actual archived transitions with N=5 and a 10 ns clock; not a new simulation or board measurement |

There are sixteen selected images across fourteen projects. The photographs and
screenshots retain their source pixels. The BMC plot is a new presentation of
stored simulation data, explicitly labeled as an archived run.
Three of the four images from the earlier Office review are byte-for-byte
copies. The camera-platform JPEG contained GPS metadata: its EXIF/XMP/IPTC/comment
segments were removed without re-encoding the JPEG scan. Decoded pixel equality
was checked against the source. No GPS metadata is published in that asset.

`content/media-sources.json` records source labels, slide/document context and
published SHA-256 hashes. It additionally records source hashes for
metadata-cleaned images and the archived BMC waveform. Full local paths, extracted contact sheets, review manifests
and complete research documents remain outside the published repository.

## Deeper Office review

The follow-up review searched 144 research Word/PowerPoint packages in the
owner-provided doctoral folder. Image relationships were mapped to slide text;
candidate sheets and the final four images were inspected before selection.
Administrative documents and personal financial/application files were excluded
from this research-media search.

| Selected source | Context used |
| --- | --- |
| Sweat-pressure presentation, slide 6 | Original interior photograph; the nRF52840 marking is visible |
| PressiBLE user manual ver2 | Embedded device-readout screenshot; document explicitly identifies PressiBLE |
| Physarum_Microgravity presentation, slides 5 and 7 | Physical RPM photograph and ESP32-S3/OV5640 hardware context; retained as historical integration |
| Space-biomedical presentation, slide 12 | Own-project manifold assembly, separate from the deck's cited satellite literature |

Chinese and English captions state what each image shows and which conclusions
it cannot support. The old wearable hardware and newer app view are not presented
as one matched test revision. No new sensing, imaging or fluid experiment was run.

## Additional folder review

The next pass indexed media/document filenames under the owner-provided ChatGPT,
Codex, PlatformIO and home folders, then inspected relevant candidates. A filename
inventory is not a visual review of every file. Six general progress, experiment
and project-poster packages were opened, alongside standalone device screenshots
and the Stop-Flow integration photograph. Source documents remain local.

Theses and oral-defense presentations, including figures extracted from them,
are excluded from publication. The PVA photograph comes from a general progress
report's microchannel-fabrication section (slides 12 and 21), not a thesis or
defense deck. Borrowed literature figures and biological-subject results in the
same report were not selected.

The ThermoPatch July screenshot belongs to the older Android interface; it is not
presented as ThermoPatchV2, nRF54L15 firmware validation or the v1.0.1 test revision.
The Galaxy Watch screenshot was selected from four near-duplicate on-demand views.
The Stop-Flow photograph was checked against its project assets and progress-report
context. Photos/screenshots were exported with text/EXIF/XMP/IPTC/comment metadata
removed where present; decoded pixel equality was verified after export.

For BMC, the existing WLF was converted with the installed Questa `wlf2vcd` tool.
The plot uses the saved VCD transitions over 140-352 ns; final stored counters are
15 checks and 0 errors. The testbench uses N=5 and a 10 ns clock. Timeout transitions
at 205/235, 285/295 and 345/351 ns were checked against the VCD. The conversion date
is not a simulation-run date. No RTL was rerun for this image, and the testbench
time scale is not the default 500 ms hardware configuration.

## Remaining image gaps

Two pages still have no selected photograph or screenshot: nRF54L15/MLX90614 and
Taipei Bus Live. Their purpose, architecture, workflow, results, analysis and scope
remain available in both languages. nRF54 candidates were mainly dense wiring,
very long UI captures, stale companion-app states and later CAD candidates that
do not match the documented public firmware revision. No suitable own-project
Taipei Bus screenshot was found; images from unrelated commercial bus apps are
not substituted. These gaps are retained rather than filled with weak evidence.

## Not selected

The review excluded cluttered bench views, tiny terminal captures, repeated
frames, slide backgrounds, logos, other people's portraits, generic illustrations
and generated apparatus renders. A weighted-graph raster with overlapping edge
labels was also excluded; its clearer shortest-path tree was retained.

The previously reviewed sweat-pressure screenshot with unrelated phone status
information remains excluded. The newer selection uses the cleaner original
device view embedded in the manual. Manual photographs matching files labeled as
generated images, and clean-looking hardware pictures with uncertain provenance,
were excluded rather than described as physical evidence. An unlabeled-context
physiological trend and clinical/subject imagery were not published. Borrowed
satellite figures, breadboard clutter, sideways photos and a thermal image lacking
defined acceptance criteria were also excluded. Images are not added just to
populate a gallery; explanatory diagrams are not experimental results.

## Sources and verification

Public README files were checked through the GitHub connector. Source snapshots:

- ThermoPatch `6c0871d`; archived v1.0.1 release/test material.
- SpaceCellCam `f78a64a`; capture sequence and configuration.
- Space BMC `5117feb`; published 15-check Questa simulation record.
- nRF54L15/MLX90614 `6a502ab`; hardware, BLE and power-analysis documents.
- Galaxy Watch `6a75d5f`; tracker lifecycle and SDK requirements.
- Taipei Bus `6d9db5e`; data, route model, UI and tests.
- Medical imaging `f80beaf`; historical metrics and reviewed aggregate plots.
- Data structures `9e9d2f7`; archived graph images and verification records.
- AFPGA curated public checkout; Lab 8 source and archived result image.

The unchanged Taipei Bus snapshot's Node test suite was executed in the earlier source-review pass:
61 tests passed, zero failed. This is software evidence, not a measurement of road
position or arrival accuracy. No device flashing, acquisition experiment, model
training or new clinical evaluation was performed.

Selected photographs and screenshots were inspected individually against their
source context and bilingual captions. No patient images or personal profiles
were selected. The BMC visualization was additionally checked against stored
signal transitions and final test counters.

## Maintenance

`content/case_studies.json` is the editable source for all sixteen pages, their
language pairs, source links and galleries. Run `python tools/build_case_studies.py`
after changing content. It also adds a detail-page link to every homepage card.
Use `python tools/build_share_images.py` after changing project names or tags.

Before adding a photo, inspect it at full size and in the actual responsive page.
Give it a precise caption, identify whether it is a prototype, archived result,
analysis output or simulation, and confirm that it provides information worth
the reading space it occupies.
