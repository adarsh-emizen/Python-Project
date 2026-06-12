def generate_insights(revenue, avg, top_product):
    if revenue > 200000:
        return f"Strong business performance. {top_product} is the top product. Focus on scaling it."
    else:
        return "Business needs improvement."