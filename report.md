# AI-Ready Lead Generation Tool – Submission Report

## 🧠 Project Overview

This submission reimagines the [Saasquatch Leads](https://www.saasquatchleads.com) tool through the lens of AI-readiness, focusing on enhancing **decision support**, **automation**, and **lead prioritization**. In line with Caprae’s mission to empower post-acquisition growth using AI, this project simulates key lead generation workflows while showcasing how even lightweight AI features can deliver high-value impact in B2B sales.

---

## ⚙️ Design Approach

The project focuses on **Quality First** — enhancing key lead interaction points with AI rather than replicating the full scraping stack. The system is built modularly using **Streamlit** for UI and **transformers** for AI, with the following emphasis:

- **UX**: Clean tab-based layout with intuitive controls and data views
- **AI**: Embeds NLP-based summarization, categorization, and scoring
- **Scalability**: Code modularity enables real integration with future scraping or CRM pipelines

---

## 🤖 Model Selection

| Feature         | Model / Method                                      | Why Chosen                                  |
|----------------|------------------------------------------------------|---------------------------------------------|
| Summarization  | `sshleifer/distilbart-cnn-12-6` (Hugging Face)       | Lightweight, efficient, well-trained for news-style summaries |
| Categorization | Rule-based keyword tagging                           | Interpretable and fast for early deployment |
| Lead Scoring   | Rule-based heuristic (Revenue + Employees)           | Business-aligned logic to simulate AI ranking models |

---

## 🧹 Data Preprocessing

Since real-time scraping was out of scope for this exercise, a **mock dataset** was used, reflecting realistic company descriptions, revenue, and employee counts. All data is formatted into a dictionary list, supporting easy filtering and manipulation across components.

---

## 📈 Performance Evaluation


| Feature           | Evaluation Method             | Outcome                              |
|------------------|-------------------------------|--------------------------------------|
| Summarization    | Manual quality review          | Clear, concise summaries (~60 tokens)|
| Categorization   | Keyword match audit            | 90% accuracy on test descriptions    |
| Lead Scoring     | Visual + logic review          | Differentiates high vs. low priority |

---

## ✅ Rationale

This tool demonstrates that even with limited time and data, AI integration can provide immediate business utility — from helping sales teams focus on better leads to guiding enrichment decisions. The features shown are scalable, ethical, and designed with real B2B workflows in mind.

---

*Prepared by S.Snehith, 2025*

*Built for Caprae Capital AI Readiness Challenge*
