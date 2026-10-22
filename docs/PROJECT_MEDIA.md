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

There are eleven selected images across nine projects. All retain their source
visual contents. Three of the four newly selected Office images are byte-for-byte
copies. The camera-platform JPEG contained GPS metadata: its EXIF/XMP/IPTC/comment
segments were removed without re-encoding the JPEG scan. Decoded pixel equality
was checked against the source. No GPS metadata is published in that asset.

`content/media-sources.json` records source labels, slide/document context and
published SHA-256 hashes. It additionally records the source hash for the
metadata-cleaned JPEG. Full local paths, extracted contact sheets, review manifests
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

## Remaining image gaps

Seven pages still have no selected photograph or screenshot: ThermoPatch, Space
BMC Core, nRF54L15/MLX90614, Galaxy Watch Sensor Monitor, Taipei Bus Live, Smart
Stop-Flow and Passive PVA Sponge Pump. Their purpose, architecture, workflow,
results, analysis and scope remain available in both languages. The folder search
did not identify suitable, reliably attributable result images for these pages.
Similar-looking apparatus and later sperm-sorting devices are not substituted
for the Stop-Flow or PVA projects.

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

The seven owner-provided research images were inspected individually against
their documents and captions. No patient images or personal profiles were selected.

## Maintenance

`content/case_studies.json` is the editable source for all sixteen pages, their
language pairs, source links and galleries. Run `python tools/build_case_studies.py`
after changing content. It also adds a detail-page link to every homepage card.
Use `python tools/build_share_images.py` after changing project names or tags.

Before adding a photo, inspect it at full size and in the actual responsive page.
Give it a precise caption, identify whether it is a prototype, archived result,
analysis output or simulation, and confirm that it provides information worth
the reading space it occupies.
