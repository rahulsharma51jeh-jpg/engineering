# BEU 101401 — Transportation Engineering · Semester Exam Notes

**[📄 Open the notes (95 pages, PDF)](BEU_101401_Transportation_Engineering_Notes.pdf)**
— GitHub previews it in the browser; use the **Download** button on that page to save it.

Bihar Engineering University · B.Tech Civil Engineering · Course Code 101401

## What's in the PDF

| Part | Pages | Contents |
|---|---|---|
| Front matter | 1–5 | Cover, how to use, **BEU exam pattern**, unit-wise weightage & priority, contents |
| Unit 1 | 6–17 | Highway development & planning, road classification, current projects, alignment, surveys |
| Unit 2 | 18–36 | Geometric design — cross-section, sight distance, horizontal & vertical alignment |
| Unit 3 | 37–47 | Traffic engineering — characteristics, studies, flow theory, capacity |
| Unit 4 | 48–60 | Regulation & control, signals, intersections, parking, lighting |
| Unit 5 | 61–70 | Pavement materials — soil, aggregates, bitumen, mixes, concrete |
| Unit 6 | 71–83 | Design of pavements — flexible, rigid, Westergaard, joints |
| Formula sheet | 84–87 | Every formula, two-column cards + standard-values table |
| Question bank | 88–95 | 2-mark & 14-mark banks (cross-referenced) + model paper with answer key |

- **47 labelled diagrams** drawn from scratch (also in `figs/` as individual PNGs)
- **51 tables**, **37 fully solved numericals**, **25 repeat-question callouts**
- The PDF has **bookmarks** — use your reader's sidebar to jump to any section

## Accuracy

Every numerical answer was verified against independent Python calculations (181 checks).
Two honest caveats, both flagged inside the document:

- The **Nagpur Plan length formula** is defined inconsistently across textbooks; use the
  symbol definitions printed on your own question paper.
- The question bank is **compiled and reworded from the recurring BEU/AKU pattern** —
  it is not a set of verbatim past papers.

## Regenerating

```bash
pip install reportlab matplotlib
cd src
python3 figs_u12.py && python3 figs_u34.py && python3 figs_u56.py   # rebuild figures
python3 build.py                                                    # rebuild the PDF
```

## References used

Khanna, Justo & Veeraragavan — *Highway Engineering* (10th ed.) · Kadiyali — *Traffic
Engineering and Transport Planning* · Partha Chakraborty & Animesh Das — *Principles of
Transportation Engineering* · Mannering & Washburn · Srinivasa Kumar · Wright & Dixon ·
IRC 37-2018, IRC 58-2015, IRC 73, IRC 86, IRC 65, IRC 93, IRC 106, IRC 67, IRC 35, IS 73, IS 2386

---
*This branch only adds this folder — nothing in the main branch was touched.
Delete it any time with:* `git push origin --delete beu-101401-notes`
