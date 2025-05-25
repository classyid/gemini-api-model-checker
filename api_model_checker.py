import os
import time
from google import genai
from google.genai import types

# Set API key
os.environ['GOOGLE_API_KEY'] = "<APIKEY>"

def test_basic_connection():
    """Test koneksi dasar dengan API"""
    try:
        print("🔧 Testing basic API connection...")
        client = genai.Client()
        
        # Test dengan request paling sederhana
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents="Hi"
        )
        
        print("✅ Basic connection successful")
        return True, client
        
    except Exception as e:
        print(f"❌ Basic connection failed: {e}")
        return False, None

def check_text_models(client):
    """Check model text generation"""
    print("\n📝 TESTING TEXT MODELS")
    print("=" * 40)
    
    text_models = [
        # Gemini 2.5 Series (Newest)
        "gemini-2.5-flash-preview-05-20",
        "gemini-2.5-pro-preview-05-06",
        
        # Gemini 2.0 Series
        "gemini-2.0-flash",
        "gemini-2.0-flash-lite",
        "gemini-2.0-flash-live-001",
        
        # Gemini 1.5 Series (Most Common)
        "gemini-1.5-flash",
        "gemini-1.5-flash-8b",
        "gemini-1.5-pro",
        
        # Legacy models
        "gemini-1.0-pro",
        "text-bison-001",
        "chat-bison-001"
    ]
    
    results = {"available": [], "need_billing": [], "not_found": [], "quota_limited": []}
    
    for model in text_models:
        print(f"🧪 Testing {model}...")
        try:
            response = client.models.generate_content(
                model=model,
                contents="Test"
            )
            print(f"   ✅ {model} - AVAILABLE")
            results["available"].append(model)
            time.sleep(1)  # Rate limiting
            
        except Exception as e:
            error_msg = str(e)
            
            if "billing" in error_msg.lower():
                print(f"   💳 {model} - NEEDS BILLING")
                results["need_billing"].append(model)
            elif "429" in error_msg or "quota" in error_msg.lower():
                print(f"   ⏳ {model} - QUOTA LIMITED")
                results["quota_limited"].append(model)
            elif "404" in error_msg or "not found" in error_msg.lower():
                print(f"   ❌ {model} - NOT FOUND")
                results["not_found"].append(model)
            else:
                print(f"   ❓ {model} - ERROR: {error_msg[:50]}...")
                results["not_found"].append(model)
    
    return results

def check_image_models(client):
    """Check model image generation"""
    print("\n🖼️  TESTING IMAGE MODELS")
    print("=" * 40)
    
    image_models = [
        # Gemini 2.0 with image generation
        "gemini-2.0-flash-preview-image-generation",
        
        # Imagen 3 (Latest)
        "imagen-3.0-generate-002",
        
        # Legacy Imagen models
        "imagen-3.0-fast-generate-001", 
        "imagegeneration@006",
        "imagen-002"
    ]
    
    results = {"available": [], "need_billing": [], "not_found": [], "quota_limited": []}
    
    for model in image_models:
        print(f"🧪 Testing {model}...")
        try:
            # Test dengan request minimal
            response = client.models.generate_images(
                model=model,
                prompt="test",
                config=types.GenerateImagesConfig(
                    number_of_images=1
                )
            )
            print(f"   ✅ {model} - AVAILABLE")
            results["available"].append(model)
            time.sleep(2)  # Rate limiting untuk image
            
        except Exception as e:
            error_msg = str(e)
            
            if "billing" in error_msg.lower():
                print(f"   💳 {model} - NEEDS BILLING")
                results["need_billing"].append(model)
            elif "429" in error_msg or "quota" in error_msg.lower():
                print(f"   ⏳ {model} - QUOTA LIMITED")  
                results["quota_limited"].append(model)
            elif "404" in error_msg or "not found" in error_msg.lower():
                print(f"   ❌ {model} - NOT FOUND")
                results["not_found"].append(model)
            else:
                print(f"   ❓ {model} - ERROR: {error_msg[:50]}...")
                results["not_found"].append(model)
    
    return results

def check_video_models(client):
    """Check model video generation"""
    print("\n🎬 TESTING VIDEO MODELS")
    print("=" * 40)
    
    video_models = [
        # Veo 2 (Latest)
        "veo-2.0-generate-001",
        
        # Legacy video models
        "veo-001",
        "video-generation-001"
    ]
    
    results = {"available": [], "need_billing": [], "not_found": [], "quota_limited": []}
    
    for model in video_models:
        print(f"🧪 Testing {model}...")
        try:
            # Test dengan request minimal tanpa execute
            operation = client.models.generate_videos(
                model=model,
                prompt="test"
            )
            print(f"   ✅ {model} - AVAILABLE")
            results["available"].append(model)
            
        except Exception as e:
            error_msg = str(e)
            
            if "billing" in error_msg.lower():
                print(f"   💳 {model} - NEEDS BILLING")
                results["need_billing"].append(model)
            elif "429" in error_msg or "quota" in error_msg.lower():
                print(f"   ⏳ {model} - QUOTA LIMITED")
                results["quota_limited"].append(model)
            elif "404" in error_msg or "not found" in error_msg.lower():
                print(f"   ❌ {model} - NOT FOUND")
                results["not_found"].append(model)
            else:
                print(f"   ❓ {model} - ERROR: {error_msg[:50]}...")
                results["not_found"].append(model)
    
    return results

def check_audio_models(client):
    """Check model audio/speech and embedding"""
    print("\n🔊 TESTING AUDIO & EMBEDDING MODELS")
    print("=" * 40)
    
    # Audio models
    audio_models = [
        "gemini-2.0-flash-live-001"  # Live audio/video interaction
    ]
    
    # Embedding models
    embedding_models = [
        "gemini-embedding-exp",  # Text embeddings
        "text-embedding-004",    # Legacy embedding
        "embedding-001"          # Legacy embedding
    ]
    
    results = {"available": [], "need_billing": [], "not_found": [], "quota_limited": []}
    
    # Test audio models
    for model in audio_models:
        print(f"🧪 Testing {model} (Audio)...")
        print(f"   ❓ {model} - REQUIRES SPECIAL API TESTING")
        results["not_found"].append(f"{model} (audio)")
    
    # Test embedding models  
    for model in embedding_models:
        print(f"🧪 Testing {model} (Embedding)...")
        try:
            # Test embedding generation
            response = client.models.embed_content(
                model=model,
                content="test embedding"
            )
            print(f"   ✅ {model} - AVAILABLE")
            results["available"].append(f"{model} (embedding)")
            
        except Exception as e:
            error_msg = str(e)
            
            if "billing" in error_msg.lower():
                print(f"   💳 {model} - NEEDS BILLING")
                results["need_billing"].append(f"{model} (embedding)")
            elif "429" in error_msg or "quota" in error_msg.lower():
                print(f"   ⏳ {model} - QUOTA LIMITED")
                results["quota_limited"].append(f"{model} (embedding)")
            elif "404" in error_msg or "not found" in error_msg.lower():
                print(f"   ❌ {model} - NOT FOUND")
                results["not_found"].append(f"{model} (embedding)")
            else:
                print(f"   ❓ {model} - ERROR: {error_msg[:50]}...")
                results["not_found"].append(f"{model} (embedding)")
    
    return results

def check_specific_models():
    """Check specific models that user is interested in"""
    print("\n🎯 QUICK CHECK: POPULAR MODELS")
    print("=" * 40)
    
    client = genai.Client()
    popular_models = {
        "gemini-1.5-flash": "Most common free text model",
        "gemini-2.0-flash": "Latest multimodal model", 
        "imagen-3.0-generate-002": "Latest image generation",
        "veo-2.0-generate-001": "Latest video generation",
        "gemini-2.5-pro-preview-05-06": "Most advanced reasoning"
    }
    
    results = {}
    
    for model, description in popular_models.items():
        print(f"🧪 {model}")
        print(f"   📝 {description}")
        
        try:
            if "imagen" in model:
                # Test image generation
                response = client.models.generate_images(
                    model=model,
                    prompt="test",
                    config=types.GenerateImagesConfig(number_of_images=1)
                )
                status = "✅ AVAILABLE"
                
            elif "veo" in model:
                # Test video generation (just initiate, don't complete)
                operation = client.models.generate_videos(
                    model=model,
                    prompt="test"
                )
                status = "✅ AVAILABLE (Video)"
                
            else:
                # Test text generation
                response = client.models.generate_content(
                    model=model,
                    contents="test"
                )
                status = "✅ AVAILABLE"
                
            print(f"   {status}")
            results[model] = "available"
            
        except Exception as e:
            error_msg = str(e)
            
            if "billing" in error_msg.lower():
                status = "💳 NEEDS BILLING"
                results[model] = "billing"
            elif "429" in error_msg or "quota" in error_msg.lower():
                status = "⏳ QUOTA LIMITED"
                results[model] = "quota"
            else:
                status = f"❌ ERROR: {error_msg[:30]}..."
                results[model] = "error"
                
            print(f"   {status}")
        
        time.sleep(1)  # Rate limiting
    
    return results

def list_available_models(client):
    """Try to list all available models"""
    print("\n📋 TRYING TO LIST ALL AVAILABLE MODELS")
    print("=" * 50)
    
    try:
        # Different ways to list models
        methods_to_try = [
            "client.models.list()",
            "client.list_models()", 
            "client.get_models()"
        ]
        
        for method in methods_to_try:
            print(f"🧪 Trying: {method}")
            try:
                if "list()" in method:
                    models = client.models.list()
                    print("   ✅ Method worked!")
                    
                    if hasattr(models, '__iter__'):
                        print("   📋 Available models:")
                        for model in models:
                            if hasattr(model, 'name'):
                                print(f"      - {model.name}")
                            elif hasattr(model, 'id'):
                                print(f"      - {model.id}")
                            else:
                                print(f"      - {model}")
                    else:
                        print(f"   📋 Response: {models}")
                    return True
                    
            except Exception as e:
                print(f"   ❌ {method} failed: {str(e)[:50]}...")
        
        print("   ❌ All listing methods failed")
        return False
        
    except Exception as e:
        print(f"❌ Error listing models: {e}")
        return False

def generate_report(text_results, image_results, video_results, audio_results):
    """Generate comprehensive report"""
    
    print("\n" + "=" * 60)
    print("📊 COMPREHENSIVE API KEY REPORT")
    print("=" * 60)
    
    # Summary statistics
    total_available = len(text_results["available"]) + len(image_results["available"]) + len(video_results["available"])
    total_billing = len(text_results["need_billing"]) + len(image_results["need_billing"]) + len(video_results["need_billing"])
    total_quota = len(text_results["quota_limited"]) + len(image_results["quota_limited"]) + len(video_results["quota_limited"])
    
    print(f"📈 SUMMARY:")
    print(f"   ✅ Available models: {total_available}")
    print(f"   💳 Need billing: {total_billing}")
    print(f"   ⏳ Quota limited: {total_quota}")
    
    # Detailed breakdown
    categories = [
        ("TEXT MODELS", text_results),
        ("IMAGE MODELS", image_results), 
        ("VIDEO MODELS", video_results),
        ("AUDIO & EMBEDDING MODELS", audio_results)
    ]
    
    for category_name, results in categories:
        print(f"\n📋 {category_name}:")
        
        if results["available"]:
            print(f"   ✅ Available: {', '.join(results['available'])}")
        
        if results["need_billing"]:
            print(f"   💳 Need billing: {', '.join(results['need_billing'])}")
            
        if results["quota_limited"]:
            print(f"   ⏳ Quota limited: {', '.join(results['quota_limited'])}")
            
        if results["not_found"]:
            print(f"   ❌ Not found: {', '.join(results['not_found'])}")
    
    # Recommendations
    print(f"\n💡 RECOMMENDATIONS:")
    
    if total_available > 0:
        print("   ✅ Your API key is working well!")
        
    if total_billing > 0:
        print("   💳 Setup GCP billing to access premium models")
        print("      → https://console.cloud.google.com/billing")
        
    if total_quota > 0:
        print("   ⏳ Wait for quota reset or setup billing for higher limits")
        
    # Save report
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"api_model_report_{timestamp}.txt"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("API KEY MODEL COMPATIBILITY REPORT\n")
        f.write("=" * 50 + "\n\n")
        
        f.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Available models: {total_available}\n")
        f.write(f"Need billing: {total_billing}\n")
        f.write(f"Quota limited: {total_quota}\n\n")
        
        for category_name, results in categories:
            f.write(f"{category_name}:\n")
            for status, models in results.items():
                if models:
                    f.write(f"  {status}: {', '.join(models)}\n")
            f.write("\n")
    
    print(f"\n💾 Report saved: {filename}")

def main():
    print("🔍 GOOGLE AI API KEY MODEL CHECKER")
    print("=" * 50)
    print("Checking which models your API key can access...")
    
    # Ask user for testing mode
    print("\nSelect testing mode:")
    print("1. Quick check (popular models only)")
    print("2. Comprehensive check (all models)")
    
    mode = input("Choose (1/2): ").strip()
    
    # Test basic connection
    connected, client = test_basic_connection()
    
    if not connected:
        print("\n❌ Cannot proceed - basic connection failed")
        return
    
    print("\n🚀 API key is working!")
    
    if mode == "1":
        # Quick check of popular models
        print("Running quick check of popular models...")
        popular_results = check_specific_models()
        
        print("\n📊 QUICK SUMMARY:")
        available = sum(1 for status in popular_results.values() if status == "available")
        billing = sum(1 for status in popular_results.values() if status == "billing")
        quota = sum(1 for status in popular_results.values() if status == "quota")
        
        print(f"✅ Available: {available}")
        print(f"💳 Need billing: {billing}")
        print(f"⏳ Quota limited: {quota}")
        
        if billing > 0:
            print("\n💡 TIP: Setup GCP billing to access premium models")
            print("   → https://console.cloud.google.com/billing")
            
    else:
        # Comprehensive check
        print("Running comprehensive check of all models...")
        
        # Check different model types
        text_results = check_text_models(client)
        image_results = check_image_models(client)
        video_results = check_video_models(client)
        audio_results = check_audio_models(client)
        
        # Try to list all models
        print("\n" + "=" * 50)
        list_available_models(client)
        
        # Generate comprehensive report
        generate_report(text_results, image_results, video_results, audio_results)
    
    print("\n✅ Model checking complete!")

if __name__ == "__main__":
    main()
